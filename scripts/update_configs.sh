#!/bin/bash

# this copies all of the config files in use to my dotfiles for easy updating/backup

cp ~/.bashrc /home/chase/dotfiles/config/bashrc # bashrc
echo 'bashrc copied'

cp ~/.config/i3/config /home/chase/dotfiles/config/i3config # i3-gaps
echo 'i3-gaps copied'

cp ~/.config/polybar/config /home/chase/dotfiles/config/polybarconfig # polybar
echo 'polybar copied'

cp ~/.config/rofi/config /home/chase/dotfiles/config/roficonfig # rofi
echo 'rofi copied'

cp ~/.config/zathura/zathurarc /home/chase/dotfiles/config/zathurarc # zathura
echo 'zathura copied'

cp ~/.config/picom/picom.conf /home/chase/dotfiles/config/picom.conf # compton
echo 'picom copied'

cp ~/.Xresources /home/chase/dotfiles/config/.Xresources
echo 'Xresources cpoied'

# latex sty files
cp -r /usr/share/texmf-dist/tex/latex/style_EHT /home/chase/dotfiles/latex_sty_files/
cp  /usr/share/texmf-dist/tex/latex/beamer/beamercolorthemegruvbox.sty /home/chase/dotfiles/latex_sty_files/beamercolorthemegruvbox.sty
echo 'latex sty files copied'

# push to git
cd /home/chase/dotfiles/
git add . -v
git commit -m 'Add existing file' -v
git push origin master -v
