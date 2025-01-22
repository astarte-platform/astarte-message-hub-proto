<!--
Copyright 2025 SECO Mind Srl

SPDX-License-Identifier: Apache-2.0
-->

# Generated proto files for C++

## Installing gRPC

Follow the [online guide](https://grpc.io/docs/languages/cpp/quickstart/#install-grpc) to install
gRPC.

## Compilation of the .proto files

The CMake scripts in this folder make it possible to generate the C++ classes and structures
starting from the .proto files.
```sh
mkdir -p ./cmake/build
pushd ./cmake/build
cmake ../..
make
popd
```
