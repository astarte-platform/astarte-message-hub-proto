#!/usr/bin/env bash

# Copyright 2023 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

PROTOC_VERSION='33.3'
version=$(protoc --version | cut -d ' ' -f 2)

if [[ $version != "$PROTOC_VERSION" ]]; then
    echo "incompatible protoc version $version, expected $PROTOC_VERSION" >&2
    exit 1
fi
