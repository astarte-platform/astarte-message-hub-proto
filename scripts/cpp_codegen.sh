#!/usr/bin/env bash

# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

set -eEuo pipefail

codegen() {
    PROTO_DIR=$1
    PROJECT_DIR=$2

    pushd $PROJECT_DIR/sample_project
    conan install . --build=missing --settings=compiler.cppstd=20
    conan build . --settings=compiler.cppstd=20
    popd

}

if [ "$1" = "codegen" ]; then
    codegen "$2" "$3"
fi
