# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

include_guard()

include(ProtoCompiler)

#[[
# astarte_setup_grpc()
#
# Configures gRPC/Protobuf dependencies and ensures standard ALIAS targets exist.
#
# Arguments (Output Variables):
#   OUT_PROTOBUF_PROTOC            - Path to the protoc executable.
#   OUT_GRPC_CPP_PLUGIN_EXECUTABLE - Path to the grpc_cpp_plugin executable.
#   OUT_PROTOBUF_STANDARD_INCLUDE_DIR - Path to standard proto includes (if needed).
#]]
function(
    astarte_setup_grpc
    OUT_PROTOBUF_PROTOC
    OUT_GRPC_CPP_PLUGIN_EXECUTABLE
    OUT_PROTOBUF_STANDARD_INCLUDE_DIR
)
    # Validate arguments
    if("${ARGC}" LESS 3)
        message(FATAL_ERROR "astarte_setup_grpc: Missing output variable arguments.")
    endif()

    option(ASTARTE_USE_SYSTEM_GRPC "Use system installed gRPC" OFF)

    # Configuration & Versioning
    if(NOT ASTARTE_USE_SYSTEM_GRPC)
        if(NOT DEFINED ASTARTE_GRPC_VERSION)
            set(ASTARTE_GRPC_VERSION "1.69.0" CACHE STRING "Version of gRPC in use.")
        elseif("${ASTARTE_GRPC_VERSION}" STREQUAL "")
            message(FATAL_ERROR "ASTARTE_GRPC_VERSION is defined but empty.")
        endif()
    endif()

    message(STATUS "--------------------------------------------------")
    message(STATUS "Astarte message hub proto configuration:")
    message(STATUS "  ASTARTE_USE_SYSTEM_GRPC:   ${ASTARTE_USE_SYSTEM_GRPC}")
    if(NOT ASTARTE_USE_SYSTEM_GRPC)
        message(STATUS "  ASTARTE_GRPC_VERSION:      ${ASTARTE_GRPC_VERSION}")
    endif()
    message(STATUS "--------------------------------------------------")

    # Internal variable holders
    set(_INT_PROTOC "")
    set(_INT_PLUGIN "")
    set(_INT_INCLUDE_DIR "")

    # Dependency Resolution
    if(ASTARTE_USE_SYSTEM_GRPC)
        find_package(Threads REQUIRED)
        option(protobuf_MODULE_COMPATIBLE ON)
        find_package(Protobuf CONFIG REQUIRED)
        find_package(gRPC CONFIG REQUIRED)

        if(CMAKE_CROSSCOMPILING)
            find_program(_INT_PROTOC protoc REQUIRED)
            find_program(_INT_PLUGIN grpc_cpp_plugin REQUIRED)
        else()
            set(_INT_PROTOC $<TARGET_FILE:protobuf::protoc>)
            set(_INT_PLUGIN $<TARGET_FILE:gRPC::grpc_cpp_plugin>)
        endif()
    else()
        include(FetchContent)
        # Set ABSL options to avoid build errors with modern gRPC
        set(ABSL_ENABLE_INSTALL ON)
        set(ABSL_PROPAGATE_CXX_STD ON)

        set(GRPC_GITHUB_URL "https://github.com/grpc/grpc.git")
        set(GRPC_GIT_TAG "v${ASTARTE_GRPC_VERSION}")

        FetchContent_Declare(
            grpc
            GIT_REPOSITORY ${GRPC_GITHUB_URL}
            GIT_TAG ${GRPC_GIT_TAG}
            GIT_SHALLOW TRUE
            GIT_PROGRESS TRUE
            GIT_CONFIG fetch.parallel=0 submodule.fetchJobs=0
        )
        FetchContent_MakeAvailable(grpc)

        # Create Standard ALIAS targets if they don't exist
        # This allows downstream code to always use "protobuf::libprotobuf"
        if(NOT TARGET protobuf::libprotobuf AND TARGET libprotobuf)
            add_library(protobuf::libprotobuf ALIAS libprotobuf)
        endif()
        if(NOT TARGET gRPC::grpc++ AND TARGET grpc++)
            add_library(gRPC::grpc++ ALIAS grpc++)
        endif()
        if(NOT TARGET gRPC::grpc++_reflection AND TARGET grpc++_reflection)
            add_library(gRPC::grpc++_reflection ALIAS grpc++_reflection)
        endif()

        # Tools
        set(_INT_PROTOC $<TARGET_FILE:protoc>)
        if(CMAKE_CROSSCOMPILING)
            find_program(_INT_PLUGIN grpc_cpp_plugin REQUIRED)
        else()
            set(_INT_PLUGIN $<TARGET_FILE:grpc_cpp_plugin>)
        endif()

        # Standard Includes
        set(_INT_INCLUDE_DIR "${grpc_SOURCE_DIR}/third_party/protobuf/src")
    endif()

    # Output Assignment
    set(${OUT_PROTOBUF_PROTOC} "${_INT_PROTOC}" PARENT_SCOPE)
    set(${OUT_GRPC_CPP_PLUGIN_EXECUTABLE} "${_INT_PLUGIN}" PARENT_SCOPE)
    set(${OUT_PROTOBUF_STANDARD_INCLUDE_DIR} "${_INT_INCLUDE_DIR}" PARENT_SCOPE)
endfunction()

#[[
# astarte_proto_attach_to_target(...)
#
# Generates C++ sources from protos and attaches them to the target.
#
# Usage:
#   astarte_proto_attach_to_target(my_target
#       PROTOBUF_PROTOC <path>
#       GRPC_CPP_PLUGIN_EXECUTABLE <path>
#       PROTOBUF_STANDARD_INCLUDE_DIR <path>
#   )
#]]
function(astarte_proto_attach_to_target TARGET_NAME)
    if(NOT TARGET "${TARGET_NAME}")
        message(FATAL_ERROR "astarte_proto_attach_to_target: Target '${TARGET_NAME}' not found.")
    endif()

    set(options PRIVATE_VISIBILITY)
    set(oneValueArgs PROTOBUF_PROTOC GRPC_CPP_PLUGIN_EXECUTABLE PROTOBUF_STANDARD_INCLUDE_DIR)
    cmake_parse_arguments(ARGS "${options}" "${oneValueArgs}" "" ${ARGN})

    message(STATUS "Attaching Astarte message hub protos to target: ${TARGET_NAME}")

    # Locate the proto directory relative to this file
    set(PROTO_BASE_DIR "${CMAKE_CURRENT_FUNCTION_LIST_DIR}/../../proto")
    get_filename_component(PROTO_BASE_DIR_ABS "${PROTO_BASE_DIR}" ABSOLUTE)
    message(STATUS "Astarte proto files source directory: ${PROTO_BASE_DIR_ABS}")

    # Ensure the specified directory actually exists
    if(NOT IS_DIRECTORY "${PROTO_BASE_DIR_ABS}")
        message(
            FATAL_ERROR
            "PROTO_BASE_DIR_ABS does not exist or is not a directory: ${PROTO_BASE_DIR_ABS}"
        )
    endif()

    # List the files explicitly
    set(PROTO_FILES
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/astarte_data.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/astarte_message.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/config.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/interface.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/message_hub_error.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/message_hub_service.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/node.proto"
        "${PROTO_BASE_DIR_ABS}/astarteplatform/msghub/property.proto"
    )

    set(PROTO_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated_astarte_protos")
    file(MAKE_DIRECTORY "${PROTO_OUTPUT_DIR}")

    set(PROTO_GENERATED_SRCS)
    set(PROTO_GENERATED_HDRS)

    # Compile Protos
    foreach(PROTO_FILE ${PROTO_FILES})
        if(NOT EXISTS "${PROTO_FILE}")
            message(FATAL_ERROR "Expected proto file not found: ${PROTO_FILE}")
        endif()
        # Calculate compile args
        set(PROTO_COMPILE_ARGS
            PROTO_FILE
            "${PROTO_FILE}"
            BASE_DIR
            "${PROTO_BASE_DIR_ABS}"
            OUTPUT_DIR
            "${PROTO_OUTPUT_DIR}"
            PROTOC_EXECUTABLE
            "${ARGS_PROTOBUF_PROTOC}"
            PLUGIN_EXECUTABLE
            "${ARGS_GRPC_CPP_PLUGIN_EXECUTABLE}"
            GENERATED_SRCS_VAR
            PROTO_GENERATED_SRCS
            GENERATED_HDRS_VAR
            PROTO_GENERATED_HDRS
        )

        # Add optional standard includes
        if(ARGS_PROTOBUF_STANDARD_INCLUDE_DIR)
            # Check include dir validity if provided
            if(NOT IS_DIRECTORY "${ARGS_PROTOBUF_STANDARD_INCLUDE_DIR}")
                message(
                    FATAL_ERROR
                    "PROTOBUF_STANDARD_INCLUDE_DIR does not exist: ${ARGS_PROTOBUF_STANDARD_INCLUDE_DIR}"
                )
            endif()
            list(
                APPEND
                PROTO_COMPILE_ARGS
                STANDARD_INCLUDE_DIR
                "${ARGS_PROTOBUF_STANDARD_INCLUDE_DIR}"
            )
        endif()

        compile_proto_file(${PROTO_COMPILE_ARGS})
    endforeach()

    if(ARGS_PRIVATE_VISIBILITY)
        target_sources(
            ${TARGET_NAME}
            PRIVATE ${PROTO_GENERATED_SRCS}
            PRIVATE
                FILE_SET private_headers
                    TYPE HEADERS
                    BASE_DIRS "${PROTO_OUTPUT_DIR}"
                    FILES ${PROTO_GENERATED_HDRS}
        )
        set(_VISIBILITY PRIVATE)
    else()
        target_sources(
            ${TARGET_NAME}
            PRIVATE ${PROTO_GENERATED_SRCS}
            PUBLIC FILE_SET HEADERS BASE_DIRS "${PROTO_OUTPUT_DIR}" FILES ${PROTO_GENERATED_HDRS}
        )
        set(_VISIBILITY PUBLIC)
    endif()

    # Link Libraries
    target_link_libraries(
        ${TARGET_NAME}
        PUBLIC gRPC::grpc++ gRPC::grpc++_reflection protobuf::libprotobuf
    )

    message(STATUS "Astarte MsgHub protos attached. Visibility: ${_VISIBILITY}")
endfunction()
