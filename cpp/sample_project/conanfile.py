# (C) Copyright 2025, SECO Mind Srl
#
# SPDX-License-Identifier: Apache-2.0

# conan install ./cpp/sample_project --build=missing
# conan build ./cpp/sample_project

from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
from conan import ConanFile
from conan.tools.build import check_min_cppstd

class Pkg(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("grpc/1.72.0")
        self.requires("protobuf/6.30.1", override = True)

    def build_requirements(self):
        self.tool_requires("protobuf/6.30.1")

    def validate(self):
        check_min_cppstd(self, 20)

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.variables["ASTARTE_USE_SYSTEM_GRPC"] = "ON"
        tc.generate()
        cmake_deps = CMakeDeps(self)
        cmake_deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
