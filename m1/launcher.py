#!/usr/bin/env python3

__version__ = '0.1'
__author__ = 'stCarolas'

import curses
import json
import logging
import os
from pathlib import Path
from os.path import expanduser
from curses import wrapper
from m1.menu import Menu
from m1.menuitem import MenuItem
from m1.menufactory import create_menu

logPath = '/Users/stCarolas/debug.log'
try:
    os.remove(logPath)
except:
    pass

def main(stdscr):
    # Clear screen
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    menu = create_menu(stdscr)

    key = ''
    while key != 'q':
        menu.draw()
        key = stdscr.getkey()
        if (key == 'KEY_DOWN'):
            menu = menu.next()
        if (key == 'KEY_UP'):
            menu = menu.prev()
        if (key == 'KEY_LEFT'):
            menu = menu.back()
        if (key == 'KEY_RIGHT'):
            menu = menu.go_in()
        if (key == '\n'):
            menu = menu.execute()
        if key not in ('KEY_DOWN','KEY_UP','KEY_LEFT','KEY_RIGHT', '\n'):
            menu = menu.handle_hotkey(key)

def show():
    wrapper(main)

if __name__ == '__main__':
        show()
