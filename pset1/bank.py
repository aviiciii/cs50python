greeting= input('Greeting: ').lower().strip()
if 'hello' in greeting:
    print('$0')
elif 'h' in greeting[0]:
    print('$20')
else:
    print('$100')

