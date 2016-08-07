#!/usr/bin/env python3

def formalize_name(name):
    if (len(name) < 24):
        spaces_to_add = 24 - len(name)
        for i in range (0, spaces_to_add):
            name = name + " "
    return name

def cut_name(name):
    if (len(name) > 50):
        return name[:18] + ".."
    return name

class MenuItem:
    def __init__(self):
        self.name = ""
        self.action = None
        self.menu = None
        self.hotkey = None
        self.generator = None
