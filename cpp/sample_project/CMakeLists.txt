# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

cmake_minimum_required(VERSION 3.23)
project(AstarteMsghubProtoSample)

add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/../.. astarte_msghub_proto)

astarte_setup_grpc(
    VAR_PROTOC_PATH           # Output: Path to the protoc executable
    VAR_GRPC_PLUGIN_PATH      # Output: Path to the grpc_cpp_plugin executable
    VAR_PROTO_STD_INC         # Output: Path to standard include directory
)

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/main.cpp" [=[
#include <iostream>
#include "astarteplatform/msghub/astarte_message.pb.h"

int main() {
    std::cout << "Hello from the inline CMake-generated main.cpp!" << std::endl;
    astarteplatform::msghub::AstarteMessage msg;
    return 0;
}
]=])

add_executable(astarte_msghub_proto_sample_project "${CMAKE_CURRENT_BINARY_DIR}/main.cpp")

astarte_proto_attach_to_target(astarte_msghub_proto_sample_project
    PROTOBUF_PROTOC                "${VAR_PROTOC_PATH}"
    GRPC_CPP_PLUGIN_EXECUTABLE     "${VAR_GRPC_PLUGIN_PATH}"
    PROTOBUF_STANDARD_INCLUDE_DIR  "${VAR_PROTO_STD_INC}"
)
