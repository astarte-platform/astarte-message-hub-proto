#!/usr/bin/env bash

# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen() {
    PROTO_DIR=$1
    PROJECT_DIR=$2

    mkdir -p $PROJECT_DIR/cmake/build
    pushd $PROJECT_DIR/cmake/build
    # TODO: remove CMake policy when updating gRPC
    cmake \
        -DPROTO_FOLDER:STRING=$PROTO_DIR \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.15 \
        -DUSE_SYSTEM_GRPC=ON \
        ../..
    cmake --build . --target astarte_msghub_proto -j $(nproc --all)
    popd

}

if [ "$1" = "codegen" ]; then
    codegen "$2" "$3"
fi
