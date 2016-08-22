#!/usr/bin/env python3

import curses
import json
import logging
from pathlib import Path
from os.path import expanduser
from curses import wrapper
from m1.menu import Menu
from m1.menuitem import MenuItem

def load_menu(menu, filepath):
    try:
        config = json.load(open(expanduser(filepath)))
        for item in config['menu']:
            menu.add_item(item)
        menu.create_hotkeys()
    except Exception as a:
            logging.warn("exception while loading menu " + str(a))

def get_local_menu():
    work_dir = Path.cwd();
    logging.debug("work_dir" + str(work_dir));
    while work_dir != None and work_dir >= Path.home() :
        if check_menu_exists(work_dir):
            return str(work_dir.joinpath(".menu")) 
        else:
            work_dir = work_dir.parent
    return None
    
def check_menu_exists(path):
    return path.joinpath(".menu").exists()

def create_menu(stdscr):
        menu = Menu(screen = stdscr)

        local_menu_dir  = get_local_menu();
        if local_menu_dir != None:
            logging.debug("local menu = " + local_menu_dir)
            load_menu(menu, expanduser(local_menu_dir))

        load_menu(menu, expanduser("~/.config/m1/menu"))

        logging.debug(print_menu(menu))
        return menu

def print_menu(menu):
    printed_menu =  ""
    if type(menu) == Menu:
        if menu.name != None:
            printed_menu = printed_menu + "###" + menu.name
        for item in menu.items:
            printed_menu = printed_menu + "\n" + print_menu(item)
        return printed_menu
    if menu.menu != None:
        if menu.name != None:
            printed_menu = printed_menu + "###" + menu.name
        for item in menu.menu.items:
            printed_menu = printed_menu + "\n" + print_menu(item)
    if type(menu) == MenuItem:
        if menu.name != None:
            printed_menu = printed_menu + menu.name
        if menu.action != None:
            printed_menu = printed_menu + " !" + menu.action
    return printed_menu
