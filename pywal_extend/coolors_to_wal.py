#!/bin/sh
#--------------------------------------------------------------------------------------------------------
# This is a python script designed to write a color scheme json file from an scss file generated from
# coolors.co. It's best to have the background colors first and fg color last.
#
#--------------------------------------------------------------------------------------------------------

path_to_scss = str(input('Enter .scss file path: '))
name = path_to_scss.split('.')[0].split('/')[-1]

# open coolors.co scss file 
with open(path_to_scss,'r') as c:
    S = c.read()

# get colors
colors_dark = {} # initialize color dictionary
for i in range(8):
    colors_dark[i] = S.split('\n')[23+i][9:16]
    
colors_light = {}
bg = S.split('\n')[23][9:16]
fg = S.split('\n')[30][9:16]
colors_light[0] = fg
colors_light[7] = bg
for i in range(1,7):
    colors_light[i] = S.split('\n')[23+i][9:16]

print('Creating dark theme...')
with open('/home/chase/dotfiles/colorschemes/custom/'+name+'.json','w') as f:
    f.write('{\n')
    f.write('\t"alpha": "100",\n')
    f.write('\t"special": {\n')
    f.write('\t\t"background": "'+colors_dark[0]+'",\n')
    f.write('\t\t"foreground": "'+colors_dark[7]+'",\n')    
    f.write('\t\t"cursor": "'+colors_dark[7]+'"\n')
    f.write('\t},\n')
    f.write('\t"colors": {\n')
    for i in range(8):
        f.write('\t\t"color'+str(i)+'": "'+colors_dark[i]+'",\n')
    for i in range(7):
        f.write('\t\t"color'+str(8+i)+'": "'+colors_dark[i]+'",\n')
    f.write('\t\t"color15": "'+colors_dark[7]+'"\n')
    f.write('\t}\n')
    f.write('}')
    f.close()
    
print('Creating light theme...')
with open('/home/chase/dotfiles/colorschemes/custom/'+name+'_light.json','w') as g:
    g.write('{\n')
    g.write('\t"alpha": "100",\n')
    g.write('\t"special": {\n')
    g.write('\t\t"background": "'+colors_light[0]+'",\n')
    g.write('\t\t"foreground": "'+colors_light[7]+'",\n')    
    g.write('\t\t"cursor": "'+colors_light[7]+'"\n')
    g.write('\t},\n')
    g.write('\t"colors": {\n')
    for i in range(8):
        g.write('\t\t"color'+str(i)+'": "'+colors_light[i]+'",\n')
    for i in range(7):
        g.write('\t\t"color'+str(8+i)+'": "'+colors_light[i]+'",\n')
    g.write('\t\t"color15": "'+colors_light[7]+'"\n')
    g.write('\t}\n')
    g.write('}')
    g.close()

print('Done!')
