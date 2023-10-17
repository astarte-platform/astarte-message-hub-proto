#!/usr/bin/env bash

# Copyright 2023 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen () {
    PROTO_DIR=$1
    PROJECT_DIR=$2
    OUT_DIR=$3
    DL_DIR=$4

    # Remove old code
    if [ -d "$OUT_DIR/astarteplatform" ]; then
        rm -r "$OUT_DIR/astarteplatform"
    fi

    if [ ! -d "$DL_DIR/grpc" ]; then
        cd "$DL_DIR"
        git clone -b v1.58.1 https://github.com/grpc/grpc
        cd grpc
        git submodule update --init
    fi

    if [ ! -f "$DL_DIR/grpc/grpc_python_plugin" ]; then
        cd "$DL_DIR/grpc"
        cmake .
        make -j$(nproc) grpc_python_plugin
        python3 -m pip install --upgrade pip
        python3 -m pip install termcolor
        cd -
    fi

    python3 "$PROJECT_DIR/protoc.py" "$DL_DIR/grpc/grpc_python_plugin" --proto_dir "$PROTO_DIR" --out_dir "$OUT_DIR"
    }

install_code (){
      OUT_DIR=$1
      INSTALL_DIR=$2

      install -d "$INSTALL_DIR"/astarteplatform/msghub
      install "$OUT_DIR"/astarteplatform/msghub/* "$INSTALL_DIR"/astarteplatform/msghub
}

if [ "$1" = "codegen" ]; then
  codegen "$2" "$3" "$4" "$5"
elif [ "$1" = "install_code" ]; then
    install_code "$2" "$3"
fi
