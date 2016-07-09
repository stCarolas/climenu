#!/usr/bin/env python3
import curses
import json
import subprocess
from curses import wrapper

class MenuItem:
    def __init__(self):
        self.name = ""
        self.action = ""
        self.items = []

class Menu(MenuItem):

    def add_menu(self, name, action):
        item = MenuItem()
        item.name = name
        if type(action) == str:
            item.action = action
        else:
            if 'action' in action:
                item.action = action['action']
        self.items.append(item)

    def formalize_menu_item_name(self, name):
        if (len(name) < 15):
            spaces_to_add = 15 - len(name)
            for i in range (0, spaces_to_add):
                name = name + " "
        return name

    def draw(self, window, active_row):
        row = 2
        for menuItem in self.items:
            if (active_row == row):
                window.addstr(row, 2, "--->> " + self.formalize_menu_item_name(menuItem.name) + " <<---")
            else:
                window.addstr(row, 2, "      " + self.formalize_menu_item_name(menuItem.name) + "      ")
            row = row + 1 
            window.hline(row, 1, 0, 28)
            row = row + 1


def get_local_menu():
    config = json.load(open(".m1"))
    menu = Menu()
    for key in config:
            menu.add_menu(key, config[key])
    return menu

def main(stdscr):
    # Clear screen
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    window =  stdscr.subwin(20, 30, 20, 70)
    menu = get_local_menu()

    key = ''
    active_row = 2
    while key != '\n' and key != 'q':
        if (key == 'KEY_DOWN'):
            active_row =  active_row + 2
        if (key == 'KEY_UP'):
            active_row = active_row - 2
        stdscr.clear()
        window.border()
        window.addstr(0, 2,  "Cli Menu 0.1beta")
        menu.draw(window, active_row) 
        stdscr.refresh()
        key = stdscr.getkey()
    if (key == '\n'):
        action = menu.items[int((active_row -2)/2)].action
        args = action.split(" ")
        subprocess.call(args)

if __name__ == '__main__':
    wrapper(main)
