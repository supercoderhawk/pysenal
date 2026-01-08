#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

VERSION = "0.1.4"

requirments = [
    'importlib-metadata; python_version < "3.8"',
]

setup(
    install_requires=requirments,
    version=VERSION,
    packages=find_packages(exclude=('tests',)),
)
