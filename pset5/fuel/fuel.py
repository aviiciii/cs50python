def main():
    while True:
        try:
            percentage = convert(input())
        except:
            pass
        else:
            break
    print(gauge(percentage))


def convert(fraction):
    x,y = fraction.split('/')
    x, y=int(x), int(y)
    if y==0:
        raise ZeroDivisionError
    elif y<x:
        raise ValueError
    return int(round((x/y)*100))

def gauge(percent):
    if percent <= 1:
        return'E'
    elif percent >= 99:
        return'F'
    else:
        return str(percent)


if __name__ == "__main__":
    main()






