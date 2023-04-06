from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
j = figlet.getFonts()

if len(sys.argv) == 0:
    sys.exit("Invalid Usage")

elif len(sys.argv) == 1:
    inp = input("Input: ")
    b = choice(figlet.getFonts())
    figlet.setFont(font = b)
    print("Output:", "\n",figlet.renderText(inp))

elif len(sys.argv) == 3:
    r = ["--font", "-f"]
    if sys.argv[1] in r:
        j = figlet.getFonts()
        if sys.argv[2] in j:
            j = figlet.getFonts()
            inp = input("Input: ")
            b = sys.argv[2]
            figlet.setFont(font = b)
            print("Output:", "\n",figlet.renderText(inp))
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")
