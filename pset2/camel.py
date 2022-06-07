def main():
    camel = input('Name: ')
    print('Name: ',end='')
    snake = convert(camel)
    print('')

def convert(camel):
    for character in camel:
        if character.isupper():
            print('_' + character.lower(), end='')
        else:
            print(character, end='')

main()