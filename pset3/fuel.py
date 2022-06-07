while True:
    try:
        x,y = input('Fraction: ').split('/')
        x, y=int(x), int(y)
        if y<x:
            raise Exception
        elif y==0:
            raise ZeroDivisionError
    except:
        pass
    else:
        break

percent = (x/y)*100
if percent <= 1:
    print('E')
elif percent >= 99:
    print('F')
else:
    print(f'{percent:.0f}%')