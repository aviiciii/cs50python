x = input()
x = x.split()
for word in x:
    word_index=x.index(word)
    if word_index %2 ==0:
        x.insert(word_index+1, '...')
x.pop()
for word in x:
    print(word, end="")
print("")