#!/usr/bin/env python3

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='m1',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts':
        ['m1 = m1.launcher:show']
    }
)

