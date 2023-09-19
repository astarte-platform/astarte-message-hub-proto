<!--
Copyright 2023 SECO Mind Srl

SPDX-License-Identifier: Apache-2.0
-->

# Astarte message hub protocol buffers for Python

This module provides access to the Astarte message hub protocol buffers through a Python API.

## Basic usage

Use `pip` to install the `astarte-message-hub-proto` package.

Then include and use it in your sources as follows:
```Python
from datetime import datetime, timezone
import grpc

from google.protobuf.timestamp_pb2 import Timestamp

from astarteplatform.msghub.message_hub_service_pb2_grpc import MessageHubStub
from astarteplatform.msghub.node_pb2 import Node
from astarteplatform.msghub.astarte_message_pb2 import AstarteMessage
from astarteplatform.msghub.astarte_type_pb2 import AstarteDataType, AstarteDataTypeIndividual

grpc_channel = grpc.insecure_channel("server address")
message_hub_stub = MessageHubStub(grpc_channel)

message_hub_node = Node(uuid="node uuid", interface_jsons=[b"interface 1 bin", b"interface 2 bin"])
message_hub_stream = message_hub_stub.Attach(message_hub_node)

# Transmit a very simple message
protobuf_value = AstarteDataType(astarte_individual=AstarteDataTypeIndividual(astarte_double=42.1))

protobuf_timestamp = Timestamp()
protobuf_timestamp.FromDatetime(datetime.now(tz=timezone.utc))

msg = AstarteMessage(
    'interface_name'="interface name",
    'path'="path",
    'timestamp'=protobuf_timestamp,
    'astarte_data'=protobuf_value)
message_hub_stub.Send(msg)

# Never ending receive loop
for astarte_message in message_hub_stream:
    # Parse astarte_message (AstarteMessage) as you see fit.
    print(astarte_message.interface_name)
    print(astarte_message.path)
    print(astarte_message.WhichOneof("payload"))
```
