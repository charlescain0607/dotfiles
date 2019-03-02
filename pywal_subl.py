#------------------------------------------------------------------------------------------
# This is a python script designed to extract the color scheme for a wallpaper from pywal
# and apply the scheme to several applications: zathura, sublime text, jupyter notebooks,
# and others. 
#------------------------------------------------------------------------------------------

import pywal
from lxml import etree

# get image and colors
image = pywal.wallpaper.get('/home/chase/.cache/wal/')
#image = pywal.image.get("/home/chase/dotfiles/dotfiles/Wallpapers/simple/wallhaven-440.jpg")
#colors = pywal.colors.file('')
colors = pywal.colors.get(image)
bg = colors['special']['background']
fg = colors['special']['foreground']
cursor = colors['special']['cursor']
color = [ colors['colors']['color'+str(i)] for i in range(16) ] 


# change zathura colors
with open('/home/chase/.config/zathura/zathurarc','w') as z:
    z.write('set recolor true'+'\n')
    z.write('set recolor-darkcolor "'+fg+'" \n')
    z.write('set recolor-lightcolor "'+bg+'" \n')
    z.close()

# change sublime colors
with open('/home/chase/.config/sublime-text-3/Cache/UserColors/TemplateUserColor.tmTheme') as f:
    # import xml
    t = etree.fromstring(f.read().encode('utf-8'))
    f.close()

    # assign colors
    t[0][9][1].text = bg
    t[0][9][3].text = color[1]
    t[0][9][5].text = fg
    t[0][9][7].text = color[0]
    t[0][9][9].text = fg
    t[0][11][0][1][1].text = bg
    t[0][11][0][1][3].text = color[5]
    t[0][11][0][1][5].text = fg
    t[0][11][0][1][7].text = color[3]
    t[0][11][0][1][9].text = color[3]
    t[0][11][0][1][11].text = color[2]
    t[0][11][1][5][1].text = color[5]
    t[0][11][2][5][1].text = color[3]
    t[0][11][3][5][1].text = color[5]
    t[0][11][4][5][1].text = color[5]
    t[0][11][5][5][1].text = color[5]
    t[0][11][6][5][1].text = color[14]
    t[0][11][7][5][1].text = color[8]
    t[0][11][8][5][1].text = color[13]
    t[0][11][9][5][1].text = color[10]
    t[0][11][10][5][1].text = color[7]
    t[0][11][11][5][1].text = color[13]
    t[0][11][12][5][1].text = color[14]
    t[0][11][13][5][1].text = color[12]
    t[0][11][14][5][1].text = color[11]
    t[0][11][15][5][1].text = color[9]
    t[0][11][16][5][1].text = color[9]
    t[0][11][17][5][1].text = color[9]
    t[0][11][18][5][1].text = color[9]
    t[0][11][19][5][1].text = color[8]
    t[0][11][20][5][1].text = color[9]
    t[0][11][21][5][1].text = color[13]
    t[0][11][22][5][1].text = color[14]
    t[0][11][23][5][1].text = color[9]
    t[0][11][24][5][3].text = color[13]
    t[0][11][25][5][1].text = color[9]
    t[0][11][26][5][3].text = color[10]
    t[0][11][27][5][3].text = color[14]
    t[0][11][28][5][1].text = color[11]
    t[0][11][29][5][1].text = color[8]
    t[0][11][30][5][1].text = color[9]
    t[0][11][31][5][1].text = color[8]
    t[0][11][32][5][1].text = color[9]
    t[0][11][33][5][1].text = color[2]
    t[0][11][33][5][3].text = color[5]
    t[0][11][34][5][1].text = color[11]
    t[0][11][35][5][1].text = color[8]
    t[0][11][36][5][1].text = color[14]
    t[0][11][37][5][1].text = color[12]
    t[0][11][38][5][1].text = color[12]
    t[0][11][39][5][1].text = color[12]
    t[0][11][40][5][1].text = fg
    t[0][11][41][5][1].text = color[8]
    t[0][11][41][5][3].text = color[0]

with open('/home/chase/.config/sublime-text-3/Cache/UserColors/UserColor.tmTheme','w') as f:
    f.write(etree.tostring(t).decode('utf-8'))
    f.close()


#def main():
#    """Main function."""
#    # Validate image and pick a random image if a
#    # directory is given below.
#    image = pywal.image.get("/home/chase/dotfiles/dotfiles/Wallpapers/simple/")
#    print(image)
#
#    # Return a dict with the palette.
#    # Set quiet to 'True' to disable notifications.
#    colors = pywal.colors.get(image)
#    print(colors)
#
#    # Apply the palette to all open terminals.
#    # Second argument is a boolean for VTE terminals.
#    # Set it to true if the terminal you're using is
#    # VTE based. (xfce4-terminal, termite, gnome-terminal.)
#    pywal.sequences.send(colors)
#
#    # Export all template files.
#    #pywal.export.every(colors, "~/.cache/wal/schemes/")
#
#    # Export individual template files.
#    #pywal.export.color(colors, "xresources", "/home/chase/.Xresources")
#    #pywal.export.color(colors, "shell", "/home/dylan/colors.sh")
#
#    # Reload xrdb, i3 and polybar.
#    pywal.reload.env()
#
#    # Reload individual programs.
#    pywal.reload.i3()
#    pywal.reload.xrdb()
#    pywal.reload.polybar()
#
#    # Set the wallpaper.
#    pywal.wallpaper.change(image)
#
#
#main()
#
