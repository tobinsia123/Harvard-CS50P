import re
import sys

def main():
    ad = input("IPv4 Address: ")
    x = validate(ad)
    print(x)

def validate(ip):
    if match := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip):
        one = int(match.group(1))
        two = int(match.group(2))
        three = int(match.group(3))
        four = int(match.group(4))
        if one <= 255 and two <= 255 and three <= 255 and four <= 255 :
            return True
        else :
            return False
    else :
        return False

if __name__ == "__main__":
    main()

