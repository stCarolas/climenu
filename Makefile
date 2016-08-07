all: install_to_home

install:
	cp Examples/tmux_menu.py /home/stcarolas/.config/m1/generators
	cp Examples/vim_projects.py /home/stcarolas/.config/m1/generators
	cp Examples/deploy_projects.py /home/stcarolas/.config/m1/generators
	cp Examples/menu /home/stcarolas/.config/m1/
	

install_to_home:
	pip3 install --upgrade --force-reinstall --user ./m1
	cp Examples/tmux_menu.py ~/.config/m1/generators
	cp Examples/vim_projects.py ~/.config/m1/generators
	cp Examples/deploy_projects.py ~/.config/m1/generators
	cp Examples/menu ~/.config/m1/

