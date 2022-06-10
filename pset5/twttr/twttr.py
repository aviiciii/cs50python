def main():
    inpt= input('Input: ')
    devowelised_text = shorten(inpt)
    print('Output:', devowelised_text)

def shorten(word):
    # vowels = ['a','e','i','o','u','A','E','I','O','U']
    # the below line cause a bug
    vowels = ['a','e','i','o','u',]
    for vowel in vowels:
        if vowel in word:
            word = word.replace(vowel, '')
    return word
if __name__ == "__main__":
    main()






