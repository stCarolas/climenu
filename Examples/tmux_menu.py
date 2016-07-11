#!/usr/bin/env python3
import subprocess
if __name__ == '__main__':
    processResult = subprocess.run(["tmux", "list-session"], stdout = subprocess.PIPE)
    stdout = processResult.stdout.decode("utf-8")
    sessions = stdout.split("\n")

    names = []
    for session in sessions:
        name = session.split(":")[0]
        if (name != None and len(name) >0):
            names.append(name)

    menu = []
    for name in names:
        menuItem = dict()
        menuItem['name'] = name
        menuItem['action'] = "vim ."
        menu.append(menuItem)
    print(menu)
