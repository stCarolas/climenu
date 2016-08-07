#!/usr/bin/env python3

import curses
import json
import logging
from pathlib import Path
from os.path import expanduser
from curses import wrapper
from menu import Menu
from menuitem import MenuItem
from menufactory import create_menu

logging.basicConfig(filename='/Users/stCarolas/debug.log',level=logging.DEBUG)
__version__ = '0.1'

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
