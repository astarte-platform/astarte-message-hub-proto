# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

# Minimum CMake required
cmake_minimum_required(VERSION 3.15)

# Project
project(astarte-msg-hub-proto)

include(FetchContent)

option(USE_SYSTEM_GRPC "Use system installed gRPC" OFF)
if(USE_SYSTEM_GRPC)
    # Protobuf
    set(protobuf_MODULE_COMPATIBLE TRUE)
    find_package(Protobuf CONFIG REQUIRED)
    message(STATUS "Using protobuf ${protobuf_VERSION}")
    set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)

    # gRPC
    find_package(gRPC CONFIG REQUIRED)
    message(STATUS "Using gRPC ${gRPC_VERSION}")
    set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)
else()
    if(MSVC)
      add_definitions(-D_WIN32_WINNT=0x600)
    endif()

    find_package(Threads REQUIRED)

    set(ABSL_ENABLE_INSTALL ON)
    set(ABSL_PROPAGATE_CXX_STD ON)

    # Show git progress since
    Set(FETCHCONTENT_QUIET FALSE)
    message(STATUS "Using gRPC via add_subdirectory (FetchContent).")
    FetchContent_Declare(
      grpc
      GIT_REPOSITORY https://github.com/grpc/grpc.git
      GIT_TAG        v1.69.0
      GIT_SHALLOW    TRUE
      GIT_PROGRESS   TRUE
      # A value of 0 will give some reasonable default
      GIT_CONFIG     fetch.parallel=0 submodule.fetchJobs=0
    )
    FetchContent_MakeAvailable(grpc)

    # Since FetchContent uses add_subdirectory under the hood, we can use
    # the grpc targets directly from this build.
    set(_PROTOBUF_LIBPROTOBUF libprotobuf)
    set(_REFLECTION grpc++_reflection)
    set(_PROTOBUF_PROTOC $<TARGET_FILE:protoc>)
    set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:grpc_cpp_plugin>)
endif()

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

    # When using protoc from FetchContent the protobuf  source have to be included manually
    if(USE_SYSTEM_GRPC)
        add_custom_command(
            OUTPUT "${out_proto_src}" "${out_proto_hdr}" "${out_grpc_src}" "${out_grpc_hdr}"
            COMMAND ${_PROTOBUF_PROTOC}
            ARGS --grpc_out "${OUT_FOLDER}"
                --cpp_out "${OUT_FOLDER}"
                -I "${PROTO_FOLDER}"
                --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
                "${proto_file}"
          DEPENDS "${proto_file}")
    else()
        set(PROTOBUF_INCLUDE_FOLDER "${CMAKE_CURRENT_LIST_DIR}/cmake/build/_deps/grpc-src/third_party/protobuf/src")
        add_custom_command(
            OUTPUT "${out_proto_src}" "${out_proto_hdr}" "${out_grpc_src}" "${out_grpc_hdr}"
            COMMAND ${_PROTOBUF_PROTOC}
            ARGS --grpc_out "${OUT_FOLDER}"
                --cpp_out "${OUT_FOLDER}"
                -I "${PROTOBUF_INCLUDE_FOLDER}"
                -I "${PROTO_FOLDER}"
                --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}"
                "${proto_file}"
          DEPENDS "${proto_file}")
    endif()



endforeach()

# Create a custom target to generate protobuf and gRPC files
add_custom_target(generate_protos ALL DEPENDS ${generated_files})
