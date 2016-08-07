#!/usr/bin/env python3

from setuptools import setup, find_packages
from os.path import join, dirname
import m1

setup(
    name='m1',
    version=m1.__version__,
    packages=find_packages(),
    entry_points={
        'console_scripts':
            ['m1 = m1:show']
    }
)

