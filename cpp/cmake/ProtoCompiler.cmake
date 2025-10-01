# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

include_guard()

#[[
# compile_proto_file(...)
#
# Compiles a single .proto file to C++ and gRPC source files.
#
# Arguments:
#   PROTO_FILE (required)             - The full path to the input .proto file.
#   BASE_DIR (required)               - The base include directory for all proto files.
#   OUTPUT_DIR (required)             - The directory where generated files will be placed.
#   PROTOC_EXECUTABLE (required)      - The path to the protoc compiler.
#   PLUGIN_EXECUTABLE (required)      - The path to the grpc_cpp_plugin.
#   GENERATED_SRCS_VAR (required)     - The name of the variable in the parent scope to which
#                                       the generated .cc file paths will be appended.
#   GENERATED_HDRS_VAR (required)     - The name of the variable in the parent scope to which
#                                       the generated .h file paths will be appended.
#   STANDARD_INCLUDE_DIR (optional)   - Path to Google's standard protobuf includes.
#]]
function(compile_proto_file)
    set(options "")
    set(one_value_args
        PROTO_FILE
        BASE_DIR
        OUTPUT_DIR
        PROTOC_EXECUTABLE
        PLUGIN_EXECUTABLE
        GENERATED_SRCS_VAR
        GENERATED_HDRS_VAR
        STANDARD_INCLUDE_DIR)
    set(multi_value_args "")
    cmake_parse_arguments(ARGS "${options}" "${one_value_args}" "${multi_value_args}" ${ARGN})

    # Get path components to build the output paths
    get_filename_component(_PROTO_INTERNAL_DIR ${ARGS_PROTO_FILE} DIRECTORY)
    get_filename_component(_PROTO_FILE_NAME ${ARGS_PROTO_FILE} NAME_WE)
    file(RELATIVE_PATH _PROTO_REL_DIR "${ARGS_BASE_DIR}" "${_PROTO_INTERNAL_DIR}")

    # Define the full paths for all generated files
    set(_OUT_PROTO_SRC "${ARGS_OUTPUT_DIR}/${_PROTO_REL_DIR}/${_PROTO_FILE_NAME}.pb.cc")
    set(_OUT_PROTO_HDR "${ARGS_OUTPUT_DIR}/${_PROTO_REL_DIR}/${_PROTO_FILE_NAME}.pb.h")
    set(_OUT_GRPC_SRC "${ARGS_OUTPUT_DIR}/${_PROTO_REL_DIR}/${_PROTO_FILE_NAME}.grpc.pb.cc")
    set(_OUT_GRPC_HDR "${ARGS_OUTPUT_DIR}/${_PROTO_REL_DIR}/${_PROTO_FILE_NAME}.grpc.pb.h")

    # Append the generated source/header files to the variable specified by the caller
    list(APPEND ${ARGS_GENERATED_SRCS_VAR} ${_OUT_PROTO_SRC} ${_OUT_GRPC_SRC})
    set(${ARGS_GENERATED_SRCS_VAR} "${${ARGS_GENERATED_SRCS_VAR}}" PARENT_SCOPE)
    list(APPEND ${ARGS_GENERATED_HDRS_VAR} ${_OUT_PROTO_HDR} ${_OUT_GRPC_HDR})
    set(${ARGS_GENERATED_HDRS_VAR} "${${ARGS_GENERATED_HDRS_VAR}}" PARENT_SCOPE)

    # Assemble the command-line arguments for protoc
    set(_PROTOC_CMD_ARGS "")
    list(APPEND _PROTOC_CMD_ARGS --grpc_out "${ARGS_OUTPUT_DIR}")
    list(APPEND _PROTOC_CMD_ARGS --cpp_out "${ARGS_OUTPUT_DIR}")
    list(APPEND _PROTOC_CMD_ARGS -I "${ARGS_BASE_DIR}")

    if(ARGS_STANDARD_INCLUDE_DIR)
        if(IS_DIRECTORY "${ARGS_STANDARD_INCLUDE_DIR}")
            list(APPEND _PROTOC_CMD_ARGS -I "${ARGS_STANDARD_INCLUDE_DIR}")
        else()
            message(WARNING "Protobuf standard include directory (for protoc) not found: "
                    "${_PROTOBUF_STANDARD_INCLUDE_DIR}. "
                    "Standard imports in .proto files might fail.")
        endif()
    endif()

    list(APPEND _PROTOC_CMD_ARGS --plugin=protoc-gen-grpc="${ARGS_PLUGIN_EXECUTABLE}")
    list(APPEND _PROTOC_CMD_ARGS "${ARGS_PROTO_FILE}")

    # Create the custom command to generate the files
    add_custom_command(
        OUTPUT "${_OUT_PROTO_SRC}" "${_OUT_PROTO_HDR}" "${_OUT_GRPC_SRC}" "${_OUT_GRPC_HDR}"
        COMMAND ${ARGS_PROTOC_EXECUTABLE}
        ARGS ${_PROTOC_CMD_ARGS}
        DEPENDS "${ARGS_PROTO_FILE}"
                "${ARGS_PROTOC_EXECUTABLE}"
                "${ARGS_PLUGIN_EXECUTABLE}"
        COMMENT "Generating C++ and gRPC files from ${_PROTO_FILE_NAME}.proto"
    )
endfunction()
