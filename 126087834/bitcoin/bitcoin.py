import requests
import sys

try:
    response = requests.get(" insert link here, youtube doesn't allow it")
except requests.RequestException:
    sys.exit(1)
else:
    bitcoin_dict = response.json()
    bitcoin_price = bitcoin_dict["bpi"]["USD"]["rate_float"]

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        print(f"${n * bitcoin_price:,.4f}")

