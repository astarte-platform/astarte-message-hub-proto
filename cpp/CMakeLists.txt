# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

# Minimum CMake required
cmake_minimum_required(VERSION 3.15)

# Project definition
project(astarte-msg-hub-proto VERSION 0.8.0 LANGUAGES CXX)

# At least C++ 17 is required
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Project configuration
option(ASTARTE_USE_SYSTEM_GRPC "Use system installed gRPC" OFF)
set(DEFAULT_PROTOBUF_VERSION "29.0.0" CACHE STRING "Default version of protobuf.")
set(DEFAULT_GRPC_VERSION "1.69.0" CACHE STRING "Default version of gRPC.")

if (ASTARTE_USE_SYSTEM_GRPC)
    if(NOT DEFINED ASTARTE_PROTOBUF_VERSION)
        set(ASTARTE_PROTOBUF_VERSION "${DEFAULT_PROTOBUF_VERSION}" CACHE STRING "Version of proto buffer to use for Astarte.")
        message(STATUS "ASTARTE_PROTOBUF_VERSION was not set, defaulting to ${ASTARTE_PROTOBUF_VERSION}")
    else()
        message(STATUS "ASTARTE_PROTOBUF_VERSION set to ${ASTARTE_PROTOBUF_VERSION}")
    endif()
endif()

if(NOT DEFINED ASTARTE_GRPC_VERSION)
    set(ASTARTE_GRPC_VERSION "${DEFAULT_GRPC_VERSION}" CACHE STRING "Version of gRPC to use for Astarte.")
    message(STATUS "ASTARTE_GRPC_VERSION was not set, defaulting to ${ASTARTE_GRPC_VERSION}")
else()
    message(STATUS "ASTARTE_GRPC_VERSION set to ${ASTARTE_GRPC_VERSION}")
endif()

include(FetchContent)

if(ASTARTE_USE_SYSTEM_GRPC)
    # Protobuf
    find_package(Protobuf ${ASTARTE_PROTOBUF_VERSION} CONFIG REQUIRED)
    message(STATUS "Using system protobuf ${protobuf_VERSION}")
    find_program(_PROTOBUF_PROTOC protoc REQUIRED)

    # gRPC
    find_package(gRPC ${ASTARTE_GRPC_VERSION} CONFIG REQUIRED)
    message(STATUS "Using system gRPC ${gRPC_VERSION}")
    set(_GRPC_CPP gRPC::grpc++)
    find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin REQUIRED)
else()
    # Required settings for windows
    if(MSVC)
      add_definitions(-D_WIN32_WINNT=0x600)
    endif()

    # gRPC needs Threads
    find_package(Threads REQUIRED)

    # Enable installation of dependencies
    set(ABSL_ENABLE_INSTALL ON)
    set(ABSL_PROPAGATE_CXX_STD ON)

    # Fetch gRPC, includes Protobuf as a submodule
    Set(FETCHCONTENT_QUIET FALSE)
    message(STATUS "Using gRPC via add_subdirectory (FetchContent).")
    FetchContent_Declare(
      grpc
      GIT_REPOSITORY https://github.com/grpc/grpc.git
      GIT_TAG        "v${ASTARTE_GRPC_VERSION}"
      GIT_SHALLOW    TRUE
      GIT_PROGRESS   TRUE
      GIT_CONFIG     fetch.parallel=0 submodule.fetchJobs=0
    )
    FetchContent_MakeAvailable(grpc)

    message(STATUS "Fetched gRPC source directory: ${grpc_SOURCE_DIR}")

    set(_GRPC_CPP gRPC::grpc++)

    #if cross-compiling, find host programs
    if(CMAKE_CROSSCOMPILING)
        find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin REQUIRED)
    else()
        set(_PROTOBUF_PROTOC $<TARGET_FILE:protoc>)
        set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:grpc_cpp_plugin>)
    endif()

    # Define the include folder for standard protobuf types (any.proto, etc.)
    set(_PROTOBUF_STANDARD_INCLUDE_DIR "${grpc_SOURCE_DIR}/third_party/protobuf/src")
    message(STATUS "Protobuf std include directory (for protoc): ${_PROTOBUF_STANDARD_INCLUDE_DIR}")
endif()

# Define where generated files will go relative to the binary directory
set(_PROTO_GENERATED_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
file(MAKE_DIRECTORY "${_PROTO_GENERATED_OUTPUT_DIR}")
message(STATUS "Generated files output directory: ${_PROTO_GENERATED_OUTPUT_DIR}")

# Directory containing proto files (default to ../proto relative to this file)
if(NOT DEFINED PROTO_FOLDER)
    set(PROTO_FOLDER "${CMAKE_CURRENT_LIST_DIR}/../proto")
endif()
message(STATUS "Proto files source directory: ${PROTO_FOLDER}")

# Collect all .proto files
file(GLOB_RECURSE proto_files "${PROTO_FOLDER}/astarteplatform/msghub/*.proto")
if(NOT proto_files)
    message(FATAL_ERROR "No .proto files found in ${PROTO_FOLDER}/astarteplatform/msghub/")
endif()

set(_proto_generated_sources)
set(_proto_generated_headers)

# Compile all .proto files
foreach(proto_file ${proto_files})
    get_filename_component(proto_dir ${proto_file} DIRECTORY)
    get_filename_component(proto_name ${proto_file} NAME_WE)
    file(RELATIVE_PATH proto_rel_dir "${PROTO_FOLDER}" "${proto_dir}")

    set(out_proto_src "${_PROTO_GENERATED_OUTPUT_DIR}/${proto_rel_dir}/${proto_name}.pb.cc")
    set(out_proto_hdr "${_PROTO_GENERATED_OUTPUT_DIR}/${proto_rel_dir}/${proto_name}.pb.h")
    set(out_grpc_src "${_PROTO_GENERATED_OUTPUT_DIR}/${proto_rel_dir}/${proto_name}.grpc.pb.cc")
    set(out_grpc_hdr "${_PROTO_GENERATED_OUTPUT_DIR}/${proto_rel_dir}/${proto_name}.grpc.pb.h")

    list(APPEND _proto_generated_sources ${out_proto_src} ${out_grpc_src})
    list(APPEND _proto_generated_headers ${out_proto_hdr} ${out_grpc_hdr})

    set(PROTOC_CMD_ARGS "")
    list(APPEND PROTOC_CMD_ARGS --grpc_out "${_PROTO_GENERATED_OUTPUT_DIR}")
    list(APPEND PROTOC_CMD_ARGS --cpp_out "${_PROTO_GENERATED_OUTPUT_DIR}")
    list(APPEND PROTOC_CMD_ARGS -I "${PROTO_FOLDER}")

    if(NOT ASTARTE_USE_SYSTEM_GRPC)
        if(IS_DIRECTORY "${_PROTOBUF_STANDARD_INCLUDE_DIR}")
            list(APPEND PROTOC_CMD_ARGS -I "${_PROTOBUF_STANDARD_INCLUDE_DIR}")
        else()
            message(WARNING "Protobuf standard include directory (for protoc) NOT FOUND: ${_PROTOBUF_STANDARD_INCLUDE_DIR}. Standard imports in .proto files might fail.")
        endif()
    endif()

    list(APPEND PROTOC_CMD_ARGS --plugin=protoc-gen-grpc="${_GRPC_CPP_PLUGIN_EXECUTABLE}")
    list(APPEND PROTOC_CMD_ARGS "${proto_file}")

    add_custom_command(
        OUTPUT "${out_proto_src}" "${out_proto_hdr}" "${out_grpc_src}" "${out_grpc_hdr}"
        COMMAND ${_PROTOBUF_PROTOC}
        ARGS ${PROTOC_CMD_ARGS}
        DEPENDS "${proto_file}"
                "${_PROTOBUF_PROTOC}"
                "${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        COMMENT "Generating C++ and gRPC files from ${proto_name}.proto"
    )
endforeach()

add_library(astarte_msghub_proto ${_proto_generated_sources})

# Link the library against required dependencies (gRPC, Protobuf, Threads).
target_link_libraries(astarte_msghub_proto
    PUBLIC
        ${_GRPC_CPP}
        protobuf::libprotobuf
)

# Add include directories for the generated headers and the original proto source directory
target_include_directories(astarte_msghub_proto
    PRIVATE
        "${_PROTO_GENERATED_OUTPUT_DIR}" # For compiling this library's sources
    PUBLIC
        # For consumers building alongside this project (e.g., via FetchContent)
        "$<BUILD_INTERFACE:${_PROTO_GENERATED_OUTPUT_DIR}>"
)

include(GNUInstallDirs)

install(
    TARGETS astarte_msghub_proto
    EXPORT astarte_msghub_proto
    LIBRARY
        DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE
        DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME
        DESTINATION ${CMAKE_INSTALL_BINDIR}
)

# create pkg-conf .pc for astarte_device_sdk
set(PC_NAME "astarte_message_hub_proto")
set(PC_DESCRIPTION "Astarte MessageHub Proto")
set(PC_VERSION ${PROJECT_VERSION})
set(PC_REQUIRES "grpc++ grpc protobuf")
set(PC_REQUIRES_PRIVATE "")
set(PC_LIB "-lastarte_msghub_proto")
set(PC_LIBS_PRIVATE "")
configure_file(
    pkg-config-template.pc.in
    astarte_message_hub_proto.pc
    @ONLY
)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/astarte_message_hub_proto.pc  DESTINATION lib/pkgconfig)
