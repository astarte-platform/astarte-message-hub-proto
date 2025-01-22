# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

# Minimum CMake required
cmake_minimum_required(VERSION 3.15)

# Project
project(astarte-msg-hub-proto)

# Protobuf
set(protobuf_MODULE_COMPATIBLE TRUE)
find_package(Protobuf CONFIG REQUIRED)
message(STATUS "Using protobuf ${protobuf_VERSION}")

# Protobuf-compiler
set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)

# gRPC
find_package(gRPC CONFIG REQUIRED)
message(STATUS "Using gRPC ${gRPC_VERSION}")
set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)

# Output directory
if(NOT DEFINED OUT_FOLDER)
    set(OUT_FOLDER "${CMAKE_CURRENT_LIST_DIR}")
endif()
message(STATUS "Output directory for generated files: ${OUT_FOLDER}")

# Directory containing proto files
if(NOT DEFINED PROTO_FOLDER)
    set(PROTO_FOLDER "${CMAKE_CURRENT_LIST_DIR}/../proto")
endif()
message(STATUS "Proto files directory: ${PROTO_FOLDER}")
# Collect all .proto files
file(GLOB_RECURSE proto_files "${PROTO_FOLDER}/astarteplatform/msghub/*.proto")

# List of outputs
set(generated_files)

foreach(proto_file ${proto_files})
    get_filename_component(proto_name ${proto_file} NAME_WE)

    # Output paths
    set(out_proto_src "${OUT_FOLDER}/astarteplatform/msghub/${proto_name}.pb.cc")
    set(out_proto_hdr "${OUT_FOLDER}/astarteplatform/msghub/${proto_name}.pb.h")
    set(out_grpc_src "${OUT_FOLDER}/astarteplatform/msghub/${proto_name}.grpc.pb.cc")
    set(out_grpc_hdr "${OUT_FOLDER}/astarteplatform/msghub/${proto_name}.grpc.pb.h")

    # Add generated files to the list
    list(APPEND generated_files ${out_proto_src} ${out_proto_hdr} ${out_grpc_src} ${out_grpc_hdr})

    # Generated sources
    add_custom_command(
        OUTPUT "${out_proto_src}" "${out_proto_hdr}" "${out_grpc_src}" "${out_grpc_hdr}"
        COMMAND ${_PROTOBUF_PROTOC}
        ARGS --grpc_out "${OUT_FOLDER}"
            --cpp_out "${OUT_FOLDER}"
            -I "${PROTO_FOLDER}"
            --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
            "${proto_file}"
      DEPENDS "${proto_file}")
endforeach()

# Create a custom target to generate protobuf and gRPC files
add_custom_target(generate_protos ALL DEPENDS ${generated_files})
