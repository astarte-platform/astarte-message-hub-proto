#!/usr/bin/env bash

# Copyright 2023 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen () {
    PROTO_DIR=$1
    PROJECT_DIR=$2
    OUT_DIR=$3

    # Remove old code
    if [ -f "$OUT_DIR/astarte-message-hub-proto/src/astarteplatform.msghub.rs" ]; then
        rm "$OUT_DIR/astarte-message-hub-proto/src/astarteplatform.msghub.rs"
    fi

    cargo run --manifest-path "$PROJECT_DIR"/Cargo.toml -p rust-codegen -- -p "$PROTO_DIR" -o "$OUT_DIR"
}

install_code (){
  OUT_DIR=$1
  INSTALL_DIR=$2

  install "$OUT_DIR"/astarteplatform.msghub.rs "$INSTALL_DIR"/astarte-message-hub-proto/src/astarteplatform.msghub.rs
}

if [ "$1" = "codegen" ]; then
  codegen "$2" "$3" "$4"
elif [ "$1" = "install_code" ]; then
    install_code "$2" "$3"
fi
