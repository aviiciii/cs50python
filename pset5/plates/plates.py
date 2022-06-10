def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check for length
    if len(s)>6 or len(s)<2:
        return False
    # check alphanumeric
    elif not s.isalnum():
        return False
    # check first 2 elements are alphabets
    elif not (s[0].isalpha() and s[1].isalpha()):
        return False
    #find first number
    first_num=len(s)-1
    for character in s:
        if character.isnumeric():
            # check if first number is zero bugged
            #if character=='0':
                # return False
            first_num = s.index(character)
            break
    # check if there is no alphabet after first num
    for character in s:
        if s.index(character)<= first_num:
            pass
        else:
            if character.isalpha():
                return False
    #all conditions satisfied
    return True


if __name__ == '__main':
    main()