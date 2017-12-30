#!/usr/bin/env python3

import os
import sys
from m1.menu import Menu
from m1.menuitem import MenuItem

def create_menu():
    menu = Menu()
    for line in sys.stdin:
        menu.add_item(line.strip())
    menu.create_hotkeys()
    return menu
