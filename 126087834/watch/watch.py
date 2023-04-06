import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(code):
    if match := re.search(r'(?:src="http).+\/embed\/(.+?)"', code):
        return f'https://youtu.be/{match.group(1)}'

if __name__ == "__main__":
    main()

