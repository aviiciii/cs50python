from validators import email


def main():
    inpt = input('What is your email address? '.strip())
    if email(inpt) == True:
        print('Valid')
    else:
        print('Invalid')



if __name__ == '__main__':
    main()