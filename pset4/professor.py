import random

def main():

    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        ans = str(x+y)
        res = 0

        for i in range(4):
            if i == 3:
                print(x, '+', y, '=', ans)
                break

            print(x, '+', y, '=', end=' ')
            res = input()
            if res!=ans:
                print('EEE')
            else:
                score+=1
                break

    print('Score: ', score)

def get_level():
    while True:
        try:
            level = input('Level: ')
            if level.isnumeric():
                level = int(level)
            else:
                raise Exception
            if 0 < level and level < 4:
                return level
            else:
                raise Exception
        except:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)

if __name__ == "__main__":
    main()