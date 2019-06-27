#------------------------------------------------------------------------------------------
# This is a python script designed to extract the color scheme for a wallpaper from pywal
# and apply the scheme to several applications: zathura, sublime text, jupyter notebooks,
# and others. 
#------------------------------------------------------------------------------------------

import pywal
import numpy as np
from lxml import etree

# rgb and hex functions
def rgb_to_hex(r,g,b):
    h='#'
    for c in [r,g,b]:
        h += hex( int(min(255,c)) )[2:].zfill(2)
    return h

def hex_to_rgb(hex):
    h = hex.lstrip('#')
    h_rgb = np.array([int(h[i:i+2], 16) for i in (0, 2 ,4)])
    return h_rgb

def brighten_hex(hex,scale):
    return rgb_to_hex(*(hex_to_rgb(hex)*scale).astype(int))

# get image and colors
image = pywal.wallpaper.get('/home/chase/.cache/wal/')
#colors = pywal.colors.file('')
colors = pywal.colors.get(image)
bg = colors['special']['background']
fg = colors['special']['foreground']
input_color = brighten_hex(bg,1.5) # brighten bg for input areas
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


# change jupyter colors
with open('/home/chase/.jupyter/custom/custom.css','w') as f:
    # write in the variables
    f.write(':root { \n')
    f.write('\t --bg: '+bg+'; \n')
    f.write('\t --fg: '+fg+'; \n')
    f.write('\t --input_color: '+input_color+'; \n')
    f.write('\t --color0: '+color[0]+'; \n')
    f.write('\t --color1: '+color[1]+'; \n')
    f.write('\t --color2: '+color[2]+'; \n')
    f.write('\t --color3: '+color[3]+'; \n')
    f.write('\t --color4: '+color[4]+'; \n')
    f.write('\t --color5: '+color[5]+'; \n')
    f.write('\t --color6: '+color[6]+'; \n')
    f.write('\t --color7: '+color[7]+'; \n')
    f.write('\t --color8: '+color[8]+'; \n')
    f.write('\t --color9: '+color[9]+'; \n')
    f.write('\t --color10: '+color[10]+'; \n')
    f.write('\t --color11: '+color[11]+'; \n')
    f.write('\t --color12: '+color[12]+'; \n')
    f.write('\t --color13: '+color[13]+'; \n')
    f.write('\t --color14: '+color[14]+'; \n')
    f.write('\t --color15: '+color[15]+'; \n')
    f.write('} \n')
    
    with open('/home/chase/.jupyter/custom/templatecustom.css') as g:
        f.write(g.read())


# change homepage colors
