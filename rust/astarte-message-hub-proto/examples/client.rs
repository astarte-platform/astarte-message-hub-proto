// This file is part of Astarte.
//
// Copyright 2025 SECO Mind Srl
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// SPDX-License-Identifier: Apache-2.0

use std::time;

use astarte_message_hub_proto::astarte_data::AstarteData as InnerData;
use astarte_message_hub_proto::astarte_message::Payload;
use astarte_message_hub_proto::message_hub_client::MessageHubClient;
use astarte_message_hub_proto::pbjson_types::Empty;
use astarte_message_hub_proto::AstarteData;
use astarte_message_hub_proto::AstarteDatastreamIndividual;
use astarte_message_hub_proto::AstarteMessage;
use astarte_message_hub_proto::Node;
use chrono::Utc;
use clap::Parser;
use log::info;
use tonic::metadata::MetadataValue;
use tonic::transport::channel::Endpoint;
use uuid::Uuid;

/// Create a ProtoBuf client for the Astarte message hub.
#[derive(Parser, Debug)]
#[clap(version, about)]
struct Cli {
    /// UUID to be used when registering the client as an Astarte message hub node.
    uuid: String,

    /// Stop after sending COUNT messages.
    #[clap(short, long)]
    count: Option<u64>,

    /// Milliseconds to wait between messages.
    #[clap(short, long, default_value = "3000")]
    time: u64,
}

#[tokio::main]
async fn main() {
    env_logger::init();
    let args = Cli::parse();

    let uuid = Uuid::parse_str(&args.uuid).unwrap();

    let channel = Endpoint::from_static("http://[::1]:50051")
        .connect()
        .await
        .unwrap();

    // adding the interceptor layer will include the Node ID inside the metadata
    let mut client =
        MessageHubClient::with_interceptor(channel, move |mut req: tonic::Request<()>| {
            req.metadata_mut()
                .insert_bin("node-id-bin", MetadataValue::from_bytes(uuid.as_ref()));
            Ok(req)
        });

    let device_datastream_interface: &str = r#"{
        "interface_name": "org.astarte-platform.rust.examples.datastream.DeviceDatastream",
        "version_major": 0,
        "version_minor": 1,
        "type": "datastream",
        "ownership": "device",
        "mappings": [
            {
                "endpoint": "/uptime",
                "type": "string",
                "explicit_timestamp": true
            }
        ]
    }"#;

    let interfaces_json = vec![device_datastream_interface.to_string()];
    let node = Node::new(interfaces_json);

    let mut stream = client.attach(node.clone()).await.unwrap().into_inner();

    // Start a separate task to handle incoming data
    let reply_handle = tokio::spawn(async move {
        info!("Waiting for messages from the message hub.");

        while let Some(astarte_message) = stream.message().await.unwrap() {
            println!("Received AstarteMessage = {astarte_message:?}");
        }

        info!("Done receiving messages, closing the connection.");
    });

    // Start a separate task to publish data
    let send_handle = tokio::spawn(async move {
        let now = time::SystemTime::now();
        let mut count = 0;
        // Consistent interval of 3 seconds
        let mut interval = tokio::time::interval(std::time::Duration::from_millis(args.time));

        while args.count.is_none() || Some(count) < args.count {
            // Wait a little
            interval.tick().await;

            println!("Publishing the uptime through the message hub.");

            let elapsed = now.elapsed().unwrap().as_secs();

            let elapsed_str = format!("Uptime for node {}: {}", args.uuid, elapsed);
            let msg = AstarteMessage {
                interface_name: "org.astarte-platform.rust.examples.datastream.DeviceDatastream"
                    .to_string(),
                path: "/uptime".to_string(),
                payload: Some(Payload::DatastreamIndividual(AstarteDatastreamIndividual {
                    data: Some(AstarteData {
                        astarte_data: Some(InnerData::String(elapsed_str)),
                    }),
                    timestamp: Some(Utc::now().into()),
                })),
            };
            client.send(msg).await.unwrap();

            count += 1;
        }

        info!("Done sending messages, closing the connection.");
        client.detach(Empty {}).await.expect("Detach failed");
    });

    let res = tokio::join!(reply_handle, send_handle);

    match res {
        (Ok(_), Ok(_)) => (),
        (Err(e), Ok(_)) | (Ok(_), Err(e)) => panic!("Error: {e}"),
        (Err(e1), Err(e2)) => panic!("Error:\n\t{e1}\n\t{e2}"),
    }
}
