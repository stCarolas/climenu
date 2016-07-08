#!/usr/bin/env python3
import curses
import json
from curses import wrapper

class Menu:
    def __init__(self):
        self.name = "Cli Menu 0.1beta"
        self.items = []
        self.items.append(MenuHeader())
        self.items.append(MenuItem())

class MenuItem:
    def __init__(self):
        self.name = "color test"
        self.action = "echo test"

class MenuHeader(MenuItem):
    def __init__(self):
        self.name = "Cli Menu"

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    window =  stdscr.subwin(20, 30, 20, 70)
    window.border()

    fileConfig = open("m1.json")
    fileStr = fileConfig.read()

    # menu = Menu()
    # row = 0
    # activeRow = 2;
    #for menuItem in menu.items:
    #    if (activeRow == row):
    #        window.addstr(row, 2, "--->>   " + menuItem.name + "   <<---")
    #    else:
    #        window.addstr(row, 2, "        " + menuItem.name + "        ")
    #    row = row + 1 
    #    window.hline(row, 1, 0, 28)
    #    row = row + 1

    #stdscr.refresh()
    #key = stdscr.getkey()

wrapper(main)
