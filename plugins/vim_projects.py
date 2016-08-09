#!/usr/bin/env python3
import json
import copy
from os import walk, listdir
from os.path import expanduser
from pathlib import Path

def check_dir(path):
    rootPath = str(path)
    if Path(rootPath).joinpath("build.gradle").exists():
        return True
    if Path(rootPath).joinpath("pom.xml").exists():
        return True
    if Path(rootPath).joinpath("Makefile").exists():
        return True

def get_menu():
    projects_dir_path = expanduser("~/Coding/projects")
    p = Path(expanduser(projects_dir_path))

    subdirs = []
    for subdir in p.iterdir():
        if subdir.is_dir() and check_dir(subdir):
            subdirs.append(subdir)

    menuItems = []
    for subdir in subdirs:
        menuItem = dict()
        menuItem['name'] = subdir.name
        menuItem['action'] =  "vim " + str(subdir.resolve())
        menuItems.append(menuItem)
    menu = {"menu":menuItems}
    return menu

if __name__ == '__main__':
    print(json.dumps(get_menu()))
