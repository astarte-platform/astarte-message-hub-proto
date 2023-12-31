<!--
Copyright 2023 SECO Mind Srl

SPDX-License-Identifier: Apache-2.0
-->

# Astarte message hub proto

This repository contains the `.proto` files used by the Astarte message hub as well as by any
client that wishes to connect itself to the message hub.

## Code generation

This project contains a Makefile that allows you to generate code for all supported languages.
Currently, the following languages are supported:
- Rust
- Python.

### Build 

Build everything and generate the code for the various languages.
```shell
make
```

### Install 

Install all language code files generated by the `all` rule in the repo folder.
```shell
make install
```

### Build language

Build and generate code for specific language.
```shell
make rust
```

### Install the generated code

Install language-code files generated by the `<lang>` rule in the repo folder.
```shell
make rust-install
```

### Help

Run `help` for more details on the rules defined in the makefile:
```shell
make help
```