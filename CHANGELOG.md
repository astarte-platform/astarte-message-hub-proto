# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.8.4] - 2025-07-17

### Fixed

- Avoid setting `CMAKE_CXX_STANDARD` and `CMAKE_CXX_STANDARD_REQUIRED` and use
  `target_compile_features` to specify the minimum required C++ version.
  [#93](https://github.com/astarte-platform/astarte-message-hub-proto/pull/93)

## [0.8.3] - 2025-07-08

### Fixed

- Lock the project's Python dependencies to the versions used by the proto stubs.
  [#90](https://github.com/astarte-platform/astarte-message-hub-proto/pull/90)

## [0.8.2] - 2025-06-26

### Changed

- CMake minor corrections in the C++ project for library installation.

## [0.8.1] - 2025-06-20

### Added

- CMake install steps have been added to the C++ project.
- CMake steps for pkg-conf have been added to the C++ project.

## [0.8.0] - 2025-06-17

### Added

- Get properties API. [astarte-device-sdk-rust#290](https://github.com/astarte-platform/astarte-device-sdk-rust/issues/290)
- Support for C++.

### Changed

- Bump protoc version to 29.0 for C++ and Python and 29.3 for Rust.
- Bump gRPC version to 1.69.0.
- Bump Rust MSRV to 1.78.0.

## [0.7.0] - 2024-09-02

### Added

- Dynamic introspection API. [#46](https://github.com/astarte-platform/astarte-message-hub-proto/pull/46)
- Add `grpc_socket_host` optional field to the `ConfigMessage` to configure the server IP to bind. [#57]

### Changed

- Send Empty parameter instead of Node in the Detach rpc. [#54](https://github.com/astarte-platform/astarte-message-hub-proto/pull/54)
- Make the `grpc_socket_port` field optional for the `ConfigMessage`, the default port will be
  `50051` on the server. [#57]
- The Attach rpc now returns a `MessageHubEvent`, which can either be an error or an Astarte message. [#56](https://github.com/astarte-platform/astarte-message-hub-proto/pull/56)
- The information about the Node sent in an Attach rpc now contains only the node introspection, since
  the Node ID is sent inside the rpc metadata. [#58](https://github.com/astarte-platform/astarte-message-hub-proto/pull/58)

[#57]: https://github.com/astarte-platform/astarte-message-hub-proto/pull/57

## [0.6.2] - 2024-04-23

### Changed

- Bump Rust MSRV to 1.72.0.
- Update protoc to version 26.1

## [0.6.1] - 2023-12-21

### Changed

- Rust: lower the minimum bound for the library dependencies

## [0.6.0] - 2023-12-13

### Added

- Configuration message to be used to send configuration to the Astarte message hub.

### Changed

- Bump Rust version to 1.66.1.

## [0.5.1] - 2023-10-11

### Added

- Initial Astarte Message Hub Proto release.
