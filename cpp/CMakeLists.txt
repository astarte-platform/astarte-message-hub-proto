# Copyright 2025 SECO Mind Srl
# SPDX-License-Identifier: Apache-2.0

# Minimum CMake required
cmake_minimum_required(VERSION 3.23)

# Project definition
project(AstarteMsghubProto VERSION 0.9.0 LANGUAGES CXX)

# Setup library options
option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

# Configuration options for this library
option(ASTARTE_USE_SYSTEM_GRPC "Use system installed gRPC" OFF)
if(NOT ASTARTE_USE_SYSTEM_GRPC)
    if(NOT DEFINED ASTARTE_GRPC_VERSION)
        set(_DEFAULT_GRPC_VERSION "1.69.0" CACHE STRING "Default version of gRPC.")
        set(ASTARTE_GRPC_VERSION "${_DEFAULT_GRPC_VERSION}" CACHE STRING "Version of gRPC in use.")
    endif()
endif()

message(STATUS "--------------------------------------------------")
message(STATUS "Astarte message hub proto configuration:")
message(STATUS "  ASTARTE_USE_SYSTEM_GRPC:   ${ASTARTE_USE_SYSTEM_GRPC}")
if(NOT ASTARTE_USE_SYSTEM_GRPC)
    message(STATUS "  ASTARTE_GRPC_VERSION:      ${ASTARTE_GRPC_VERSION}")
endif()
message(STATUS "--------------------------------------------------")

if(ASTARTE_USE_SYSTEM_GRPC)
    find_package(Threads REQUIRED)
    option(protobuf_MODULE_COMPATIBLE ON)
    find_package(Protobuf CONFIG REQUIRED)
    find_package(gRPC CONFIG REQUIRED)

    set(_PROTOBUF_LIBPROTOBUF protobuf::libprotobuf)
    set(_REFLECTION gRPC::grpc++_reflection)
    set(_GRPC_CPP gRPC::grpc++)
    if(CMAKE_CROSSCOMPILING)
        find_program(_PROTOBUF_PROTOC protoc)
        find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin)
    else()
        set(_PROTOBUF_PROTOC $<TARGET_FILE:protobuf::protoc>)
        set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:gRPC::grpc_cpp_plugin>)
    endif()
else()
    include(FetchContent)
    # Enable installation of dependencies
    set(ABSL_ENABLE_INSTALL ON)
    set(ABSL_PROPAGATE_CXX_STD ON)

    # Fetch gRPC, includes Protobuf as a submodule
    set(GRPC_GITHUB_URL "https://github.com/grpc/grpc.git")
    set(GRPC_GIT_TAG "v${ASTARTE_GRPC_VERSION}")
    FetchContent_Declare(
      grpc
      GIT_REPOSITORY ${GRPC_GITHUB_URL}
      GIT_TAG        ${GRPC_GIT_TAG}
      GIT_SHALLOW    TRUE
      GIT_PROGRESS   TRUE
      GIT_CONFIG     fetch.parallel=0 submodule.fetchJobs=0
    )
    FetchContent_MakeAvailable(grpc)

    # Since FetchContent uses add_subdirectory under the hood, we can use
    # the grpc targets directly from this build.
    set(_PROTOBUF_LIBPROTOBUF libprotobuf)
    set(_REFLECTION grpc++_reflection)
    set(_GRPC_CPP grpc++)
    set(_PROTOBUF_PROTOC $<TARGET_FILE:protoc>)
    if(CMAKE_CROSSCOMPILING)
        find_program(_GRPC_CPP_PLUGIN_EXECUTABLE grpc_cpp_plugin)
    else()
        set(_GRPC_CPP_PLUGIN_EXECUTABLE $<TARGET_FILE:grpc_cpp_plugin>)
    endif()

    # Define the include folder for standard protobuf types (any.proto, etc.)
    set(_PROTOBUF_STANDARD_INCLUDE_DIR "${grpc_SOURCE_DIR}/third_party/protobuf/src")
    message(STATUS "Protobuf std include directory (for protoc): ${_PROTOBUF_STANDARD_INCLUDE_DIR}")
endif()

# Define where generated files will go relative to the binary directory
set(_PROTO_OUTPUT_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
file(MAKE_DIRECTORY "${_PROTO_OUTPUT_DIR}")
message(STATUS "Generated files output directory: ${_PROTO_OUTPUT_DIR}")

# Directory containing proto files
set(_PROTO_BASE_DIR "${CMAKE_CURRENT_LIST_DIR}/../proto" CACHE PATH "Path to the .proto files")
message(STATUS "Proto files source directory: ${_PROTO_BASE_DIR}")

# Ensure the specified directory actually exists
if(NOT IS_DIRECTORY "${_PROTO_BASE_DIR}")
    message(FATAL_ERROR "_PROTO_BASE_DIR does not exist or is not a directory: ${_PROTO_BASE_DIR}")
endif()

# Explicitly list the proto files
set(_PROTO_FILES
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/astarte_data.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/astarte_message.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/config.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/interface.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/message_hub_error.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/message_hub_service.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/node.proto"
    "${_PROTO_BASE_DIR}/astarteplatform/msghub/property.proto"
)

# Include the function to process the proto files
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake")
include(ProtoCompiler)

# Set empty list for the result of the compilation
set(_PROTO_GENERATED_SRCS)
set(_PROTO_GENERATED_HDRS)

# Compile all .proto files
foreach(_PROTO_FILE ${_PROTO_FILES})
    set(_COMPILE_ARGS
        PROTO_FILE              "${_PROTO_FILE}"
        BASE_DIR                "${_PROTO_BASE_DIR}"
        OUTPUT_DIR              "${_PROTO_OUTPUT_DIR}"
        PROTOC_EXECUTABLE       "${_PROTOBUF_PROTOC}"
        PLUGIN_EXECUTABLE       "${_GRPC_CPP_PLUGIN_EXECUTABLE}"
        GENERATED_SRCS_VAR      _PROTO_GENERATED_SRCS # Passing the name, not the value
        GENERATED_HDRS_VAR      _PROTO_GENERATED_HDRS # Passing the name, not the value
    )
    if(NOT ASTARTE_USE_SYSTEM_GRPC)
        list(APPEND _COMPILE_ARGS STANDARD_INCLUDE_DIR "${_PROTOBUF_STANDARD_INCLUDE_DIR}")
    endif()
    compile_proto_file(${_COMPILE_ARGS})
endforeach()

add_library(astarte_msghub_proto)
target_compile_features(astarte_msghub_proto PUBLIC cxx_std_17)
if(MSVC)
    # Set minimum version of Windows
    target_compile_definitions(astarte_msghub_proto PRIVATE _WIN32_WINNT=0x0600)
endif()
target_sources(astarte_msghub_proto
    PUBLIC FILE_SET HEADERS
        BASE_DIRS "${_PROTO_OUTPUT_DIR}"
        FILES ${_PROTO_GENERATED_HDRS}
    PRIVATE
        ${_PROTO_GENERATED_SRCS}
)

# Link the library against required dependencies (gRPC, Protobuf).
target_link_libraries(astarte_msghub_proto
    PUBLIC
        ${_GRPC_CPP}
        ${_REFLECTION}
        ${_PROTOBUF_LIBPROTOBUF}
)

# Set required target properties
set_target_properties(astarte_msghub_proto
    PROPERTIES
        POSITION_INDEPENDENT_CODE ${BUILD_SHARED_LIBS})
set_target_properties(astarte_msghub_proto
    PROPERTIES
        ARCHIVE_OUTPUT_DIRECTORY "${AstarteMsghubProto_BINARY_DIR}"
        LIBRARY_OUTPUT_DIRECTORY "${AstarteMsghubProto_BINARY_DIR}"
        RUNTIME_OUTPUT_DIRECTORY "${AstarteMsghubProto_BINARY_DIR}"
)

include(GNUInstallDirs)
include(CMakePackageConfigHelpers)

configure_package_config_file(
    "${CMAKE_CURRENT_LIST_DIR}/cmake/Config.cmake.in"
    "${CMAKE_CURRENT_BINARY_DIR}/astarte_msghub_protoConfig.cmake"
    INSTALL_DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/astarte_msghub_proto"
)

# Generate the version file for package version checking
write_basic_package_version_file(
    "${CMAKE_CURRENT_BINARY_DIR}/astarte_msghub_protoConfigVersion.cmake"
    VERSION ${PROJECT_VERSION}
    COMPATIBILITY SameMajorVersion
)

# Install the target
install(
    TARGETS astarte_msghub_proto
    EXPORT astarte_msghub_proto-targets
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    FILE_SET HEADERS DESTINATION ${CMAKE_INSTALL_INCLUDEDIR}
)

# TODO: re-enable this once the system installation of this package has been validated
# install(
#     EXPORT astarte_msghub_proto-targets
#     FILE astarte_msghub_proto-targets.cmake
#     NAMESPACE astarte_msghub_proto::
#     DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/astarte_msghub_proto"
# )

install(
    FILES
        "${CMAKE_CURRENT_BINARY_DIR}/astarte_msghub_protoConfig.cmake"
        "${CMAKE_CURRENT_BINARY_DIR}/astarte_msghub_protoConfigVersion.cmake"
    DESTINATION "${CMAKE_INSTALL_LIBDIR}/cmake/astarte_msghub_proto"
)

# create pkg-conf .pc for astarte_msghub_proto
set(PC_NAME "astarte_msghub_proto")
set(PC_DESCRIPTION "Astarte MessageHub Proto")
set(PC_VERSION ${PROJECT_VERSION})
set(PC_REQUIRES "grpc++ protobuf")
set(PC_REQUIRES_PRIVATE "")
set(PC_LIB "-lastarte_msghub_proto")
set(PC_LIBS_PRIVATE "")
configure_file(
    "${CMAKE_CURRENT_LIST_DIR}/pkg-config-template.pc.in"
    astarte_msghub_proto.pc
    @ONLY
)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/astarte_msghub_proto.pc  DESTINATION lib/pkgconfig)
