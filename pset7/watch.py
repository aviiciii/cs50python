import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # sample : "http://www.youtube.com/embed/xvFZjo5PgG0"
    # sample : <iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>...
    if link := re.search(r"\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"",s):
        return('https://youtu.be/'+link.group(1))


if __name__ == "__main__":
    main()