import random

while True:
    try:
        level = input('Level: ')
        if level.isnumeric():
            level = int(level)
        else:
            raise Exception
        if level > 0:
            break
        else:
            raise Exception
    except:
        pass

n = random.randint(1,level)
guess=0

while guess != n:
    guess = input('Guess: ')
    if guess.isnumeric():
        guess= int(guess)
    else:
        continue
    if guess > n:
        print('Too large!')
    elif guess < n:
        print('Too small!')
    else:
        print('Just right!')
        break