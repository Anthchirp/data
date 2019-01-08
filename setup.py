#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

requirements = ["pytest", "pyyaml"]
setup_requirements = []
test_requirements = []

needs_pytest = {"pytest", "test", "ptr"}.intersection(sys.argv)
if needs_pytest:
    setup_requirements.append("pytest-runner")

setup(
    author="Markus Gerstel",
    author_email="dials-support@lists.sourceforge.net",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="DIALS Regression Data manager",
    entry_points={
        "console_scripts": ["dials.data = dials_data.cli:main"],
        "libtbx.dispatcher.script": ["dials.data = dials.data"],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    include_package_data=True,
    keywords="dials_data",
    name="dials_data",
    packages=find_packages(include=["dials_data"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/dials/data",
    version="0.2.0",
    zip_safe=False,
)
