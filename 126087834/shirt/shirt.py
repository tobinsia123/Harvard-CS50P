import sys
import os

from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    path_1 = os.path.splitext(sys.argv[1])
    path_2 = os.path.splitext(sys.argv[2])

if path_1[1] == "" or path_2[1] == "":
    sys.exit("Invalid input")
elif path_1[1].lower() != path_2[1].lower():
    sys.exit("Input and output have different extensions")
else:
    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as im:
            photo = ImageOps.fit(im, size=(600, 600))
            photo.paste(shirt, shirt)
            photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")

