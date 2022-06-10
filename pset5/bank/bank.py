def main():
    greet= input('Greeting: ')
    fine = value(greet)
    print('$'+str(fine))

def value(greeting):

    greeting = greeting.lower().strip()

    if 'hello' in greeting:
        return(0)
    elif 'h' in greeting[0]:
        return(20)
    else:
        return(10)


if __name__ == "__main__":
    main()




