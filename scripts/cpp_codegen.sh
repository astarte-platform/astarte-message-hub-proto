#!/usr/bin/env bash

# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen() {
    PROTO_DIR=$1
    PROJECT_DIR=$2

    pushd $PROJECT_DIR/sample_project
    # TODO: remove CMake policy when updating gRPC
    cmake \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.15 \
        -DASTARTE_USE_SYSTEM_GRPC=ON \
        -S . \
        -B build
    cmake --build build -j $(nproc --all)
    popd

}

if [ "$1" = "codegen" ]; then
    codegen "$2" "$3"
fi
