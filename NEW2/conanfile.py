from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps

class Recipe(ConanFile):
	settings = { "os", "compiler", "build_type", "arch" }
	name = "helloworld123"
	version = "0.1"

	exports_sources = "*"
	generators = "CMakeDeps", "CMakeToolchain"

	def build(self):
		cmake = CMake(self)
		cmake.configure()
		cmake.build()

	def package(self):
		cmake = CMake(self)
		cmake.install()

