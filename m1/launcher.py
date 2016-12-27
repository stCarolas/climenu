#!/usr/bin/env python3

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

logPath = expanduser('~/m1.log')
try:
    os.remove(logPath)
except:
    pass

logging.basicConfig(
        filename = expanduser(logPath),
        level = logging.DEBUG
)

def get_cli_args():
    parser = argparse.ArgumentParser(description='Get properties for alfalab cli')
    parser.add_argument('key',
                        metavar = 'key',
                        type = str, 
                        nargs = 1,
                        help = 'property key')
    return parser.parse_args()

def main(stdscr):
    # Init curses 
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

if __name__ == '__main__':
    # args = get_cli_args()
    # print(Config().get_value("global",args.key[0]))
    menu = create_menu()
    # wrapper(main)
