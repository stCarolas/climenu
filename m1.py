#!/usr/bin/env python3
import curses
import json
import sys
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

        if screen != None:
            curses.init_pair(1, curses.COLOR_WHITE, -1)
            self.window =  screen.subwin(20, 40, 15, 70)

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
        if self.screen == None:
            return self

        self.window.border()
        self.window.addstr(0, 2,  "  M1 Cli Menu  ")
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
                self.window.addstr(row, 2, "--->> " + title + " <<---", curses.color_pair(1))
            else:
                self.window.addstr(row, 2, "      " + title + "      ")
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
            return self.parent
        return self

    def go_in(self):
        selected_item = self.items[self.active_row - 2]
        submenu = selected_item.menu
        if submenu != None:
            return submenu
        return self

    def execute(self):
        selected_item = self.items[self.active_row - 2]

        action = selected_item.action
        if action != None:
            args = action.split(" ")
            subprocess.call(args)
            sys.exit()

        submenu = selected_item.menu
        if submenu != None:
            return submenu

        generator = selected_item.generator
        if generator != None:
            process = subprocess.run(generator.split(" "), stdout=subprocess.PIPE)
            config = json.loads(process.stdout.decode("UTF-8"))
            menu = Menu(parent = self, screen = self.screen)
            for item in config['menu']:
                menu.add_item(item)
            return menu
        return self


def load(menu, filepath):
    try:
        config = json.load(open(filepath))
        for item in config['menu']:
            menu.add_item(item)
    except:
        pass


def create_menu(stdscr):
    menu = Menu(screen = stdscr)
    load(menu, "/Users/stCarolas/.config/m1/menu")
    load(menu, "./.menu")
    return menu

def main(stdscr):
    # Clear screen
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    menu = create_menu(stdscr)

    key = ''
    while key != 'q':
        stdscr.clear()
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
