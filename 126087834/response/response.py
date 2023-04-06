import validators

def main():
    print(validate(input("What's your email address? ").strip()))

def validate(address: str):
    return "Valid" if validators.email(address) else "Invalid"

if __name__ == "__main__":
    main()