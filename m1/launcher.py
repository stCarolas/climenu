#!/usr/bin/env python3

import logging
import os
import sys
from pathlib import Path
from os.path import expanduser
from m1.menu import Menu
from m1.getch import _Getch
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

def main():
    menu = create_menu()
    for item in menu.items:
        line= item.hotkey + ": " + item.name
        # sys.stdout.write(line)
        print(line.rstrip("\n"))
    f=open("/dev/tty")
    os.dup2(f.fileno(), 0)
    key = _Getch()
    with open("/tmp/m1","w") as out:
        choice = menu.handle_hotkey(key())
        if choice != None:
            out.write(choice.strip())

if __name__ == '__main__':
    main()
