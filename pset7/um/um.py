import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):


    count=re.findall(r'\bum\b', s, re.IGNORECASE)

    return len(count)


if __name__ == "__main__":
    main()