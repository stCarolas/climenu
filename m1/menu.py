#!/usr/bin/env python3

import curses
import sys
import re
import os
import logging
import subprocess
import m1
from m1.menuitem import MenuItem

START_MENU_POSITION = 1

class Menu:
    def __init__(self):
        self.items = []
        self.hotkeys = dict()

    def add_item(self, name):
        item = MenuItem()
        item.set_name(name)
        self.items.append(item)

    def handle_hotkey(self, key):
        if key in self.hotkeys.keys():
            return self.hotkeys[key]
        return None

    def create_hotkeys(self):
        i = ord('a');
        for item in self.items:
            item.hotkey = chr(i)
            self.hotkeys[item.hotkey] = item
            i=i+1
