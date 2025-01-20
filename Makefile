# Copyright 2023 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

# This Makefile serves to generate the gRPC interface and
# the related messages from .proto file.

# we want bash as shell
SHELL := $(shell if [ -x "$$BASH" ]; then echo $$BASH; \
         else if [ -x BASH_PATH="$(command -v bash)" ]; then echo $$BASH_PATH; \
         else echo sh; fi; fi)

# Set O variable if not already done on the command line;
# or avoid confusing packages that can use the O=<dir> syntax for out-of-tree
# build by preventing it from being forwarded to sub-make calls.
ifneq ("$(origin O)", "command line")
O := $(CURDIR)/output
endif

# Remove the trailing '/.' from $(O) as it can be added by the makefile wrapper
# installed in the $(O) directory.
# Also remove the trailing '/' the user can set when on the command line.
override O := $(patsubst %/,%,$(patsubst %.,%,$(O)))
# Make sure $(O) actually exists before calling realpath on it; this is to
# avoid empty CANONICAL_O in case on non-existing entry.
CANONICAL_O := $(shell mkdir -p $(O) >/dev/null 2>&1)$(realpath $(O))

CANONICAL_CURDIR = $(realpath $(CURDIR))

PROTO_DIR = $(CANONICAL_CURDIR)/proto
RUST_LANG_DIR = $(CANONICAL_CURDIR)/rust
PYTHON_LANG_DIR = $(CANONICAL_CURDIR)/python
CPP_LANG_DIR = $(CANONICAL_CURDIR)/cpp

BASE_DIR := $(CANONICAL_O)
$(if $(BASE_DIR),, $(error output directory "$(O)" does not exist))

# download-location
DL_DIR := $(shell mkdir -p $(BASE_DIR)/dl >/dev/null 2>&1)$(BASE_DIR)/dl

BUILD_DIR := $(BASE_DIR)/build
RUST_BUILD_DIR := $(BUILD_DIR)/rust
PYTHON_BUILD_DIR := $(BUILD_DIR)/python
CPP_BUILD_DIR := $(BUILD_DIR)/cpp

FILES=$(wildcard proto/astarteplatform/msghub/*.proto)

PROTOC_CHECK_SCRIPT=$(CANONICAL_CURDIR)/scripts/protoc_check.sh

RUST_LANG=$(RUST_BUILD_DIR)/astarte-message-hub-proto
RUST_CODEGEN_SCRIPT=$(CANONICAL_CURDIR)/scripts/rust_codegen.sh

PYTHON_LANG=$(PYTHON_BUILD_DIR)/astarteplatform
PYTHON_CODEGEN_SCRIPT=$(CANONICAL_CURDIR)/scripts/python_codegen.sh

CPP_LANG=$(CPP_BUILD_DIR)/astarteplatform
CPP_CODEGEN_SCRIPT=$(CANONICAL_CURDIR)/scripts/cpp_codegen.sh

# This is our default rule, so must come first
.PHONY: all
all : $(RUST_LANG) $(PYTHON_LANG) $(CPP_LANG)

$(RUST_LANG): $(FILES) $(RUST_CODEGEN_SCRIPT)
		mkdir -p $(RUST_BUILD_DIR)
		$(RUST_CODEGEN_SCRIPT) codegen $(PROTO_DIR) $(RUST_LANG_DIR) $(RUST_BUILD_DIR)

$(PYTHON_LANG): $(FILES) $(PYTHON_CODEGEN_SCRIPT)
		mkdir -p $(PYTHON_BUILD_DIR)
		$(PYTHON_CODEGEN_SCRIPT) codegen $(PROTO_DIR) $(PYTHON_LANG_DIR) $(PYTHON_BUILD_DIR) $(DL_DIR)

$(CPP_LANG): $(FILES) $(CPP_CODEGEN_SCRIPT)
		mkdir -p $(CPP_BUILD_DIR)
		$(CPP_CODEGEN_SCRIPT) codegen $(PROTO_DIR) $(CPP_LANG_DIR) $(CPP_BUILD_DIR)

.PHONY: protoc-check
protoc-check: $(PROTOC_CHECK_SCRIPT)
		$(PROTOC_CHECK_SCRIPT)

.PHONY: rust
rust: protoc-check $(RUST_LANG)

.PHONY: python
python: protoc-check $(PYTHON_LANG)

.PHONY: cpp
cpp: protoc-check $(CPP_LANG)

.PHONY: rust-install
rust-install: $(RUST_LANG)
		$(RUST_CODEGEN_SCRIPT) install_code $(RUST_BUILD_DIR) $(RUST_LANG_DIR)

.PHONY: python-install
python-install: $(PYTHON_LANG)
		$(PYTHON_CODEGEN_SCRIPT) install_code $(PYTHON_BUILD_DIR) $(PYTHON_LANG_DIR)

.PHONY: cpp-install
cpp-install: $(CPP_LANG)
		$(CPP_CODEGEN_SCRIPT) install_code $(CPP_BUILD_DIR) $(CPP_LANG_DIR)

.PHONY: install
install: rust-install python-install cpp-install

.PHONY: clean
clean:
		rm -rf $(BUILD_DIR)

.PHONY: rust-dirclean
rust-dirclean:
		rm -rf $(RUST_BUILD_DIR)

.PHONY: python-dirclean
python-dirclean:
		rm -rf $(PYTHON_BUILD_DIR)

.PHONY: cpp-dirclean
cpp-dirclean:
		rm -rf $(CPP_BUILD_DIR)

.PHONY: help
help:
		@echo 'Cleaning:'
		@echo '  clean                  - delete all files created by build'
		@echo
		@echo 'Build:'
		@echo '  all                    - Build everything and generate the code for the various languages'
		@echo '  install                - Install files into repo folder'
		@echo
		@echo 'Language-specific:'
		@echo '  <lang>                  - Build, install <lang> and all its dependencies and generate <lang> code'
		@echo '  <lang>-install          - Install <lang> files into the repo <lang> folder'
		@echo '  <lang>-dirclean         - Remove <lang> build directory'
