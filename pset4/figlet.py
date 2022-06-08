from pyfiglet import Figlet
from sys import argv, exit
from random import choice

fig = Figlet()
font_list=fig.getFonts()

if len(argv) == 1:
    r_font = choice(font_list)
    fig.setFont(font=r_font)
elif len(argv) == 3:
    if argv[1]=='-f' or argv[1]=='--font':
        c_font = argv[2]
        if c_font not in font_list:
            exit('Invalid usage')
        fig.setFont(font=c_font)
    else:
        exit('Invalid usage')
else:
    exit('Invalid usage')
text = input('Input: ')
print(fig.renderText(text))



