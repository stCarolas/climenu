#!/usr/bin/env python3

import os
from m1.menu import Menu
from m1.getch import _Getch
from m1.menuitem import MenuItem
from m1.menufactory import create_menu

def main(with_menu = True):
    menu = create_menu()
    if with_menu:
        print_menu(menu)
    reopen_input_from_terminal()
    key = _Getch()
    with open("/tmp/m1","w") as out:
        choice = menu.handle_hotkey(key())
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

if __name__ == '__main__':
    main()
