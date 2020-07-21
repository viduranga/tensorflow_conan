# coding=utf-8
from conans import ConanFile, tools, CMake
import sys, re, os
import shutil

class TensorflowConan(ConanFile):
    name = "tensorflow"
    version = "2.2.0"
    settings = "os", "compiler", "build_type", "arch"

    def build(self):
        if self.settings.os == "Windows":
            url = "https://dl.bintray.com/viduranga/storage/tensorflow/2.2.0/lib/windows.zip"
        elif self.settings.os == "Macos"
            url = "https://dl.bintray.com/viduranga/storage/tensorflow/2.2.0/lib/macos.zip"
        elif self.settings.os == "Linux"
            url = "https://dl.bintray.com/viduranga/storage/tensorflow/2.2.0/lib/linux.zip"
        else:
            raise Exception("Binary does not exist for these settings")
        tools.get(url, filename="lib")
        tools.get("https://dl.bintray.com/viduranga/storage/tensorflow/2.2.0/include.zip")

    def package(self):
        self.copy("*") # assume package as-is, but you can also copy specific files or rearrange

    def package_info(self):  # still very useful for package consumers
        self.cpp_info.libs = ["tensorflow_cc", "tensorflow_framework"]