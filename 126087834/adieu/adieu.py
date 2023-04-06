import inflect

lst = [ ]
p = inflect.engine()

while True:
    try:
        name = input("Names: ")
        lst.append(name)
    except EOFError:
        print ("\n")
        break
for name in lst:
    mylist = p.join((lst), final_sep=",")
print(f"Adieu, adieu, to {mylist}")