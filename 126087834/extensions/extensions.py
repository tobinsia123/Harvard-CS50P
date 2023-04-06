text = input("File name: ")
x = text.lower().strip()

if x.endswith(".gif"):
    print("image/gif")

elif x.endswith(".jpg"):
    print("image/jpeg")

elif x.endswith(".jpeg"):
    print("image/jpeg")

elif x.endswith(".png"):
    print("image/png")

elif x.endswith(".txt"):
    print("text/plain")

elif x.endswith(".zip"):
    print("application/zip")

elif x.endswith(".pdf"):
    print("application/pdf")

else:
    print("application/octet-stream")