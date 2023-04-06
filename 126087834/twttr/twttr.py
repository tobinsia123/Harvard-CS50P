answer = input("Input: ")

print("Output: ", end="")

for l in answer:
    if not l.lower() in ["a", "e", "i", "o", "u"]:
        print(l, end="")

print()