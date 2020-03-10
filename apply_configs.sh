#!/bin/bash

# this puts all of my config files in the right places for easy installation

cp /home/chase/dotfiles/config/bashrc ~/.bashrc # bashrc
echo 'bashrc copied'

mkdir ~/.config/i3/config && cp /home/chase/dotfiles/config/i3config ~/.config/i3/config # i3-gaps
echo 'i3-gaps copied'

mkdir ~/.config/polybar/ && cp /home/chase/dotfiles/config/polybarconfig ~/.config/polybar/config # polybar
cp /home/chase/dotfiles/config/polylaunch.sh ~/.config/polybar/launch.sh
echo 'polybar copied'

mkdir ~/.config/rofi/ && cp /home/chase/dotfiles/config/roficonfig ~/.config/rofi/config # rofi
echo 'rofi copied'

mkdir ~/.config/zathura/ && cp /home/chase/dotfiles/config/zathurarc ~/.config/zathura/zathurarc # zathura
echo 'zathura copied'

mkdir ~/.config/compton/ && cp /home/chase/dotfiles/config/compton.conf ~/.config/compton/compton.conf # compton
echo 'compton copied'

cp /home/chase/dotfiles/config/.Xresources ~/.Xresources
echo 'Xresources cpoied'

# latex sty files
cp -r /usr/share/texmf-dist/tex/latex/style_EHT /home/chase/dotfiles/latex_sty_files/
cp  /usr/share/texmf-dist/tex/latex/beamer/beamercolorthemegruvbox.sty /home/chase/dotfiles/latex_sty_files/beamercolorthemegruvbox.sty
echo 'latex sty files copied'