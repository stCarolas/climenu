#!/usr/bin/env python3
import curses
from curses import wrapper

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()

    menu =  stdscr.subwin(20, 30, 20, 70)
    menu.border()
    menu.addstr(0, 0, "Cli Menu 0.1beta")
    menu.addstr(1, 2, "color test")
    menu.addstr(3, 2, "color test          <<---")
    menu.addstr(5, 2, "color test")
    
    curses.curs_set(0)
    menu.hline(2, 1, 0, 28);
    menu.hline(4, 1, 0, 28);
    menu.hline(6, 1, 0, 28);

    stdscr.refresh()
    stdscr.getkey()
    menu.erase()
    menu.addstr(3, 2, "color test")
    menu.addstr(5, 2, "color test          <<---")
    menu.refresh()
    stdscr.refresh()
    stdscr.getkey()
    menu.refresh()
    stdscr.refresh()
    menu.refresh()
    stdscr.getkey()

wrapper(main)
