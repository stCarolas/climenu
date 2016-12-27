#!/usr/bin/env python3

import os
import re
import json
import argparse
import subprocess
import atexit
from pathlib import Path

LIBRARY_FILE = '.theatrum'
DEFAULT_MEDIA_FILE_PATTERNS = [
            ".*\.avi",
            ".*\.mp4"
        ]
DEFAULT_COMMAND_TO_SEE_FILE = "/Applications/VLC.app/Contents/MacOS/VLC"

def get_cli_args():
    parser = argparse.ArgumentParser(description='Tool for comfortable viewing mediafiles')
    parser.add_argument('command',
                        metavar = 'command',
                        type = str, 
                        nargs = 1,
                        help = 'theatrum command')                    
    parser.add_argument('--dir',
                        dest = 'dir',
                        type = str,
                        default = '.',
                        help = 'directory with media')
    return parser.parse_args()

class Library:

    def __init__(self, path = None):
        self.path = path
        self.command_to_watch = DEFAULT_COMMAND_TO_SEE_FILE 
        self.watched_files = []
        self.create_list_of_files_to_watch()

    def create_list_of_files_to_watch(self):
        self.not_watched_files = []
        if self.path == None:
            return
        for file in os.scandir(self.path):
            for pattern in DEFAULT_MEDIA_FILE_PATTERNS:
                if re.match(pattern, file.name):
                    self.not_watched_files.append(file.name)

    def watch_next(self):
        if len(self.not_watched_files) < 1:
            return
        nextfile = self.not_watched_files[0]
        atexit.register(subprocess.run, [DEFAULT_COMMAND_TO_SEE_FILE, nextfile])
        self.not_watched_files.remove(nextfile)
        self.watched_files.append(nextfile)
        self.save()

    def garant_config_exists(self, path):
        if not Path(path).joinpath(LIBRARY_FILE).exists():
            Library(path).save()

    def save(self):
        serialized = dict()
        serialized['path'] = self.path
        serialized['command_to_watch'] = self.command_to_watch 
        serialized['watched_files'] = self.watched_files
        serialized['not_watched_files'] = self.not_watched_files
        with open(LIBRARY_FILE, "w") as config:
            config.write(json.dumps(serialized))

    def load(self, path):
        self.garant_config_exists(path)
        with open(LIBRARY_FILE, "r") as config:
            readed = json.loads(config.read())
            self.path = readed['path'] 
            self.command_to_watch = readed['command_to_watch']
            self.watched_files = readed['watched_files'] 
            self.not_watched_files = readed['not_watched_files']

def generate_menu():
    menuItems = []
    menu = {"menu": menuItems}

    lib = Library()
    lib.load(".")

    if len(lib.not_watched_files) > 0:
        item = create_menu_item(
                'view next',
                "/Users/stCarolas/Coding/projects/m1/plugins/theatrum.py next --dir " + os.curdir
        )
        menuItems.append(item)

    item = create_menu_item(
            'theatrum',
            "/Users/stCarolas/Coding/projects/m1/plugins/theatrum.py init --dir " + os.curdir
    )
    menuItems.append(item)

    return menu

def create_menu_item(name, action):
    menuItem = dict()
    menuItem['name'] = name
    menuItem['action'] = action 
    return menuItem

if __name__ == '__main__':
    args = get_cli_args()
    if args.command[0] == 'menu':
        print(generate_menu())
    if args.command[0] == 'init':
        print(generate_menu())
    if args.command[0] == 'next':
        lib = Library()
        lib.load(".")
        lib.watch_next()
