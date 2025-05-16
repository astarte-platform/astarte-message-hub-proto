<!--
Copyright 2025 SECO Mind Srl

SPDX-License-Identifier: Apache-2.0
-->

# Make file to compile the proto files for C++

## About gRPC

This project relies on gRPC to generate properly the stubs for C++.
You can either choose to install gRPC on your system or to let CMake check it out.
In production we recomend letting CMake fetch gRPC automatically, this is the default option in
the CMakeList in this folder.
If you wish to manually install CMake follow the
[online guide](https://grpc.io/docs/languages/cpp/quickstart/#install-grpc) making sure you choose
the appropriate version. Then provide CMake with the `USE_SYSTEM_GRPC` option during build.

## Import the proto files as a CMake library

The CMakeList in this folder allows you to import the proto files present in this repo as a
CMake library using FetchContent.
Use fetch content as follows replacing the tag with the wanted version:
```CMake
set(MSGHUB_PROTO_GITHUB_URL https://github.com/astarte-platform/astarte-message-hub-proto.git)
set(MSGHUB_PROTO_GIT_TAG v0.7.0)
FetchContent_Declare(
  astarte_msghub_proto
  GIT_REPOSITORY ${MSGHUB_PROTO_GITHUB_URL}
  GIT_TAG        ${MSGHUB_PROTO_GIT_TAG}
  GIT_SHALLOW    TRUE
  GIT_PROGRESS   TRUE
)
FetchContent_MakeAvailable(astarte_msghub_proto)
```
Remember to link your target with the imported library:
```CMake
target_link_libraries(app PRIVATE astarte_msghub_proto)
```
