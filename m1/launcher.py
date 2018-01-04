#!/usr/bin/env python3

import os
import argparse
from m1.menu import Menu
from m1.getch import _Getch
from m1.menuitem import MenuItem
from m1.menufactory import create_menu

def get_cli_args():
    parser = argparse.ArgumentParser(description='Generate changelog')
    parser.add_argument('--no-input',
                        dest = 'input',
                        action='store_false')
    parser.add_argument('--no-menu',
                        dest = 'menu',
                        action='store_false')
    return parser.parse_args()

def main(with_menu = True, with_input = True, key = None):
    menu = create_menu()
    if with_menu:
        print_menu(menu)
    if with_input:
        reopen_input_from_terminal()
        key = _Getch()()
    if key != None:
        with open("/tmp/m1","w") as out:
            choice = menu.handle_hotkey(key)
            if choice != None:
                out.write(choice.strip())

def print_menu(menu = None):
    if menu == None:
        return
    for item in menu.items:
        line= item.hotkey + ": " + item.name
        print(line.rstrip("\n"))
    
def reopen_input_from_terminal():
    f=open("/dev/tty")
    os.dup2(f.fileno(), 0)

def launch_from_terminal():
    args = get_cli_args()
    main(args.menu, args.input)

if __name__ == '__main__':
    launch_from_terminal()
