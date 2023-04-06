def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    valid_check = True
    digit_count = 0
    if(len(s) < 2 or len(s) > 6 ):
        valid_check = False
        return valid_check

    if(s[0].isdigit() or s[1].isdigit()):
        valid_check = False
        return valid_check

    for char in s:
        if(not char.isalnum()):
            valid_check = False
            return valid_check

        if(digit_count > 1 and char.isalpha()):
            valid_check = False
            return valid_check

        if(char.isdigit()):
            digit_count += 1

        if(digit_count == 1 and char == "0"):
            valid_check = False
            return valid_check

    return valid_check

main()

