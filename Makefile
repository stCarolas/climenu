all: install_to_home

install:
	cp plugins/tmux_menu.py /home/stcarolas/.config/m1/generators
	cp plugins/vim_projects.py /home/stcarolas/.config/m1/generators
	cp plugins/deploy_projects.py /home/stcarolas/.config/m1/generators
	cp config/menu /home/stcarolas/.config/m1/

install_to_home:
	pip3 install --upgrade --force-reinstall --user ./m1
	cp plugins/tmux_menu.py ~/.config/m1/generators
	cp plugins/vim_projects.py ~/.config/m1/generators
	cp plugins/deploy_projects.py ~/.config/m1/generators
	cp config/menu ~/.config/m1/

