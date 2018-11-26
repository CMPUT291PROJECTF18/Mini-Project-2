#!/usr/bin/python
# -*- coding: utf-8 -*-

"""setup.py for mini-project-2"""

import codecs
import re
import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test


def find_version(*file_paths):
    with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *file_paths), "r") as fp:
        version_file = fp.read()
    m = re.search(r"^__version__ = \((\d+), ?(\d+), ?(\d+)\)", version_file, re.M)
    if m:
        return "{}.{}.{}".format(*m.groups())
    raise RuntimeError("Unable to find a valid version")


VERSION = find_version("mini_project_2", "__init__.py")


class Pylint(test):
    def run_tests(self):
        from pylint.lint import Run
        Run(["mini_project_2", "--persistent", "y", "--rcfile", ".pylintrc",
             "--output-format", "colorized"])


class PyTest(test):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        test.initialize_options(self)
        self.pytest_args = "-v --cov={}".format("mini_project_2")

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


setup(
    name="mini-project-2",
    version=VERSION,
    description="CMPUT 291 Mini-Project 2",
    long_description=open("README.rst").read(),
    keywords="cmput291 project university",
    author="Nathan Klapstein, Thomas Lorincz",
    author_email="nklapste@ualberta.ca",
    url="https://github.com/CMPUT291PROJECTF18/Mini-Project-2",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "mini-project-2 = mini_project_2.__main__:main"
        ]
    },
    install_requires=[
        "bsddb3>=6.2.6,<7.0.0",
        "beautifulsoup4>=4.6.3,<5.0.0",
        "lxml>=4.2.5,<5.0.0",
    ],
    extras_require={
        "docs": [
            "sphinx>=1.7.5,<2.0.0",
            "sphinx_rtd_theme>=0.3.1,<1.0.0",
            "sphinx-autodoc-typehints>=1.3.0,<2.0.0",
            "sphinx-argparse>=0.2.2,<1.0.0",
        ],
        "tests": [
            "mock>=2.0.0,<3.0.0",
            "pytest",
            "pytest-cov",
            "pylint>=1.9.1,<2.0.0",
        ]
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    cmdclass={"test": PyTest, "lint": Pylint},
)
