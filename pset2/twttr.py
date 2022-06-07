vowels = ['a','e','i','o','u', 'A','E','I','O','U']
inpt= input('Input: ')
print('Output: ', end='')

for letter in inpt:
    if letter in vowels:
        pass
    else:
        print(letter, end='')
print('')