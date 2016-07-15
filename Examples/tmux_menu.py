#!/usr/bin/env python3
import subprocess
import json

def get_menu():
    processResult = subprocess.run(["tmux", "list-session"], stdout = subprocess.PIPE)
    stdout = processResult.stdout.decode("utf-8")
    sessions = stdout.split("\n")

    names = []
    for session in sessions:
        name = session.split(":")[0]
        if (name != None and len(name) >0):
            names.append(name)

    menuItems = []

    for name in names:
        menuItem = dict()
        menuItem['name'] = name
        menuItem['action'] = 'urxvt -hold -e tmux attach -dt ' + name
        menuItems.append(menuItem)
    menu = {"menu": menuItems}
    return menu

if __name__ == '__main__':
    print(json.dumps(get_menu()))
