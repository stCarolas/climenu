#!/usr/bin/env python3
import curses
import time
import json
import sys
import re
import os
import subprocess
from curses import wrapper

def formalize_menu_item_name(name):
    if (len(name) < 24):
        spaces_to_add = 24 - len(name)
        for i in range (0, spaces_to_add):
            name = name + " "
    return name

def cut_menu_item_name(name):
    if (len(name) > 20):
        return name[:18] + ".."
    return name

class MenuItem:
    def __init__(self):
        self.name = ""
        self.action = None
        self.menu = None
        self.generator = None

class Menu:
    def __init__(self, parent = None, screen = None):
        self.parent = parent
        self.screen = screen

        self.name = ""
        self.action = ""
        self.items = []
        self.active_row = 2
        self.window = None

        if screen != None:
            curses.init_pair(1, curses.COLOR_WHITE, -1)
            curses.init_pair(2, curses.COLOR_GREEN, -1)

    def add_item(self, json):
        item = MenuItem()
        if 'name' in json:
            item.name = cut_menu_item_name(json['name'])
        if 'action' in json:
            item.action = json['action']
        if 'generator' in json:
            item.generator = json['generator']
        if 'menu' in json:
            item.menu = Menu(parent = self, screen = self.screen)
            for sub_item in json['menu']:
                item.menu.add_item(sub_item)
        self.items.append(item)

    def draw(self):
        if self.screen != None:
            self.screen.border()
            self.screen.addstr(0, 2,  "  M1 Cli Menu  ")
        row = 2
        for menuItem in self.items:
            title = menuItem.name
            if menuItem.menu != None or menuItem.generator != None:
                title ="[ "  + title + " ]"
            else:
                title = "  " + title
            title = formalize_menu_item_name(title)
            if (self.active_row == row):
                # todo separate making title
                if self.screen != None:
                    self.screen.addstr(row, 2, "--->> " + title + " <<---", curses.color_pair(1))
            else:
                if self.screen != None:
                    self.screen.addstr(row, 2, "      " + title + "      ")
            row = row + 1 
        return self
    
    def next(self):
        self.active_row = self.active_row + 1
        return self

    def prev(self):
        self.active_row = self.active_row - 1
        return self

    def back(self):
        if self.parent != None:
            self.screen.clear()
            return self.parent
        return self

    def go_in(self):
        selected_item = self.items[self.active_row - 2]
        submenu = selected_item.menu
        if submenu != None:
            self.screen.clear()
            return submenu
        return self

    def execute(self):
        selected_item = self.items[self.active_row - 2]

        action = selected_item.action
        if action != None:
            args = action.split(" ")
            subprocess.call(args)

        submenu = selected_item.menu
        if submenu != None:
            return submenu

        generator = selected_item.generator
        if generator != None:
            args = []
            argRegexp = '(-?\S+)|(".+")'
            m = re.findall(argRegexp, generator)
            for match in m:
                match1 = match[0]
                if match1 != None and match1 != '':
                    args.append(match1)
                else:
                    args.append(match[1])
            process = subprocess.run(args, stdout=subprocess.PIPE)
            config = json.loads(process.stdout.decode("UTF-8"))
            menu = Menu(parent = self, screen = self.screen)
            for item in config['menu']:
                menu.add_item(item)
            return menu
        return self


def load(menu, filepath):
        config = json.load(open(filepath))
        for item in config['menu']:
            menu.add_item(item)


def create_menu(stdscr):
    menu = Menu(screen = stdscr)
    load(menu, "/home/stcarolas/.config/m1/menu")
    #load(menu, "./.menu")
    return menu

def main(stdscr):
    # Clear screen
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    menu = create_menu(stdscr)

    key = ''
    while key != 'q':
        menu.draw()
        stdscr.refresh()
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

if __name__ == '__main__':
    wrapper(main)
