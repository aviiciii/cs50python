def convert(word):
    if word == ":)":
        return "🙂"
    else:
        return "🙁"


def main():
    print("Enter text: ", end="")
    text = input().split()
    for word in text:
        if word == ":)" or word == ":(":
            ind = text.index(word)
            text[ind] = convert(word)
    print ("Converted: ", end="")
    for word in text:
        print(word, end=" ")
    print("")




if __name__ == "__main__":
    main()