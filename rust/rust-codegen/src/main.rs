/*
 * This file is part of Astarte.
 *
 * Copyright 2023 SECO Mind Srl
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
use std::fs;
use std::path::PathBuf;

use clap::Parser;
use color_eyre::eyre::Context;

#[derive(Parser)]
#[clap(version, about)]
struct Cli {
    /// Base path to Protocol Buffer definitions
    #[clap(short, long)]
    proto_directory: PathBuf,

    /// Output directory where to store compiled protobuf files
    #[clap(short, long)]
    out: PathBuf,
}

fn main() -> color_eyre::Result<()> {
    let cli = Cli::parse();

    color_eyre::install()?;

    if !cli.out.exists() {
        fs::create_dir_all(&cli.out)
            .wrap_err_with(|| format!("couldn't create directory {}", cli.out.display()))?;
    }

    let proto_dir = cli.proto_directory.canonicalize().wrap_err_with(|| {
        format!(
            "couldn't canonicalize working directory {}",
            cli.proto_directory.display()
        )
    })?;

    let mut config = tonic_build::configure();

    let proto_files = &[
        proto_dir.join("astarteplatform/msghub/message_hub_service.proto"),
        proto_dir.join("astarteplatform/msghub/node.proto"),
        proto_dir.join("astarteplatform/msghub/astarte_message.proto"),
        proto_dir.join("astarteplatform/msghub/astarte_type.proto"),
        proto_dir.join("astarteplatform/msghub/config.proto"),
        proto_dir.join("astarteplatform/msghub/interface.proto"),
        proto_dir.join("astarteplatform/msghub/property.proto"),
    ];

    // NOTE: This is a temporary workaround to build the documentation on docs.rs, since they are
    //       using protobuf 3.12.
    if std::env::var("DOCS_RS").is_ok() {
        config = config.protoc_arg("--experimental_allow_proto3_optional");
    }

    config
        .compile_well_known_types(true)
        .out_dir(&cli.out)
        .extern_path(".google.protobuf", "::pbjson_types")
        .compile(proto_files, &[proto_dir])
        .unwrap_or_else(|e| panic!("Failed to compile protos {:?}", e));

    Ok(())
}
