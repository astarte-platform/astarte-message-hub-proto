#!/usr/bin/env bash

# Copyright 2023 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen () {
    PROTO_DIR=$1
    PROJECT_DIR=$2
    OUT_DIR=$3
    DL_DIR=$4

    # Check if the environment and dependencies are ok
    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
    fi
    source .venv/bin/activate
    pip install --upgrade pip
    package_name="grpcio"
    package_version="1.69.0"
    installed_version=$((pip show $package_name | grep Version | awk '{print $2}') || true)
    if [ "$installed_version" != "$package_version" ]; then
        pip install $package_name==$package_version
        if [ $? -ne 0 ]; then
            echo "Failed to install $package_name version $package_version."
            exit 1
        fi
    fi
    package_name="grpcio-tools"
    package_version="1.69.0"
    installed_version=$((pip show $package_name | grep Version | awk '{print $2}') || true)
    if [ "$installed_version" != "$package_version" ]; then
        pip install $package_name==$package_version
        if [ $? -ne 0 ]; then
            echo "Failed to install $package_name version $package_version."
            exit 1
        fi
    fi
    pip install termcolor

    # Remove old code
    if [ -d "$OUT_DIR/astarteplatform" ]; then
        rm -r "$OUT_DIR/astarteplatform"
    fi

    python "$PROJECT_DIR/protoc.py" --proto_dir "$PROTO_DIR" --out_dir "$OUT_DIR"
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
  codegen "$2" "$3" "$4" "$5"
elif [ "$1" = "install_code" ]; then
    install_code "$2" "$3"
fi
