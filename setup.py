#!/usr/bin/env python3

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name            =   'm1',
    version         =   '0.1',
    author          =   'stCarolas',
    author_email    =   'stcarolas@gmail.com',
    packages        =   find_packages(),
    entry_points    =   {
                            'console_scripts': ['m1 = m1.launcher:main']
                        },
    data_files      =   [
                         ('/home/stcarolas/.config/m1/plugins', ['plugins/vim_projects.py', 'plugins/tmux_menu.py']),
                         ('/home/stcarolas/.config/m1/', ['config/menu'])
                        ]
)
