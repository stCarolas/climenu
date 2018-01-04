#!/usr/bin/env python3

def formalize_name(name):
    if (len(name) < 24):
        spaces_to_add = 24 - len(name)
        for i in range (0, spaces_to_add):
            name = name + " "
    return name

def cut_name(name):
    if (len(name) > 80):
        return name[:58] + ".."
    return name

class MenuItem:
    def __init__(self):
        self.name = ""
        self.hotkey = None

    def set_name(self, name):
        self.name = cut_name(name)
