<!--
Copyright 2025 SECO Mind Srl

SPDX-License-Identifier: Apache-2.0
-->

# Make file to compile the proto files for C++

## About gRPC

This project relies on gRPC to generate properly the stubs for C++. You can either choose to install gRPC on your system or to let CMake check it out.
In production we recomend letting CMake fetch gRPC automatically, this is the default option in the CMakeList in this folder.
If you wish to manually install CMake follow the [online guide](https://grpc.io/docs/languages/cpp/quickstart/#install-grpc) making sure you choose the appropriate version. Then provide CMake with the `ASTARTE_USE_SYSTEM_GRPC` option during build.

## Import the proto files as a CMake library

The CMakeList in this folder allows you to import the proto files present in this repo through the use of CMake functions.
The simplest way to get the protos is to use fetch content as follows replacing the tag with the wanted version:
```CMake
set(MSGHUB_PROTO_GITHUB_URL https://github.com/astarte-platform/astarte-message-hub-proto.git)
set(MSGHUB_PROTO_GIT_TAG v0.10.1)
FetchContent_Declare(
  astarte_msghub_proto
  GIT_REPOSITORY ${MSGHUB_PROTO_GITHUB_URL}
  GIT_TAG        ${MSGHUB_PROTO_GIT_TAG}
  GIT_SHALLOW    TRUE
  GIT_PROGRESS   TRUE
)
FetchContent_MakeAvailable(astarte_msghub_proto)
```
This will automatically check out the proto repository and make it available throughout your CMake build. You can also check out the repo manually and add it to your project through `add_subdirectory`.
Next use the provided functions to generate the proto C++ stubs from the proto files defined in this repo:
```CMake
# Utility function that can be used to set up gRPC
astarte_setup_grpc(
    VAR_PROTOC_PATH           # Output: Path to the protoc executable
    VAR_GRPC_PLUGIN_PATH      # Output: Path to the grpc_cpp_plugin executable
    VAR_PROTO_STD_INC         # Output: Path to standard include directory
)

# Generate the proto files and attach them to the target
astarte_proto_attach_to_target(<your-target-here>
    ${_ASTARTE_PROTO_VISIBILITY_FLAG}
    PROTOBUF_PROTOC                "${VAR_PROTOC_PATH}"
    GRPC_CPP_PLUGIN_EXECUTABLE     "${VAR_GRPC_PLUGIN_PATH}"
    PROTOBUF_STANDARD_INCLUDE_DIR  "${VAR_PROTO_STD_INC}"
)
```
