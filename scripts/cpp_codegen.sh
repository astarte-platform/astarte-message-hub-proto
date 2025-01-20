#!/usr/bin/env bash

# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen () {
    PROTO_DIR=$1
    PROJECT_DIR=$2
    OUT_DIR=$3

    # Remove old code
    if [ -d "$OUT_DIR/astarteplatform" ]; then
        rm -r "$OUT_DIR/astarteplatform"
    fi

    mkdir -p $PROJECT_DIR/cmake/build
    pushd $PROJECT_DIR/cmake/build
    cmake -DOUT_FOLDER:STRING=$OUT_DIR -DPROTO_FOLDER:STRING=$PROTO_DIR ../..
    make
    popd

    }

install_code (){
      OUT_DIR=$1
      INSTALL_DIR=$2

      # Check if the directory exists and is not empty
      if [ -d "$INSTALL_DIR"/astarteplatform/msghub ] && [ "$(ls -A "$INSTALL_DIR"/astarteplatform/msghub)" ]; then
        rm -v "$INSTALL_DIR"/astarteplatform/msghub/*
      fi

      install -d "$INSTALL_DIR"/astarteplatform/msghub
      install -m 644 "$OUT_DIR"/astarteplatform/msghub/* "$INSTALL_DIR"/astarteplatform/msghub
}

if [ "$1" = "codegen" ]; then
  codegen "$2" "$3" "$4"
elif [ "$1" = "install_code" ]; then
    install_code "$2" "$3"
fi
