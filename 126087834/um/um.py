import re

def main():
    inp: str = input("Text: ")
    print(count(inp))

def count(s: str):
    res: list[str] = re.findall(r"^um\b|(?<=\s)um\b", s, re.IGNORECASE)
    return len(res)

if __name__ == "__main__":
    main()