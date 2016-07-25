# m1

This is a cli "menu" or "app launcher" . It uses ncurses and JSON as a menu descripting format. Menus can be generated dynamically in runtime. 
Inspired by Openbox Pipe Menus.

### Installing
`make` will install libs to `~/.local/bin` and `~/.config/m1`.
`make install` will install to `/usr/local/bin`.

There are need to create some directories on these path (temporary, sorry).

### Logging
By default log is written in `debug.log` in startup directory. Config located in m1.py in code.
