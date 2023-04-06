c = input("camelcase: ")

for i in c:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

print()