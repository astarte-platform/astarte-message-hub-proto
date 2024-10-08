# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Dynamic introspection API.
- Add `grpc_socket_host` optional field to the `ConfigMessage` to configure the server IP to bind.

### Changed

- Send Empty parameter instead of Node in the detach rpc.
- Make the `grpc_socket_port` field optional for the `ConfigMessage`, the default port will be
  `50051` on the server.
- The Attach rpc now returns a `MessageHubEvent`, which can either be an error or an Astarte message.

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
