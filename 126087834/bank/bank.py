greeting = input("Greeting: ")
if greeting.lower().strip() == "hello":
    print("$0")
elif greeting.lower().strip() == "hello, newman":
    print("$0")
elif greeting.lower().strip() == "how you doing?":
    print("$20")
else:
    print("$100")