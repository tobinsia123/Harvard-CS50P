from random import randint

def main():
    questions = 10
    answer_list = []
    level = get_level()
    while questions != 0:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3
        while tries != 0:
            answer = input(f"{x} + {y} = ")
            if int(answer) != x + y:
                print("EEE")
                tries -= 1
                if tries == 0:
                    print(f"{x} + {y} = {x+y}")
                    questions -= 1
            else:
                questions -= 1
                answer_list.append(answer)
                break

    if questions == 0:
        print(f"Score: {len(answer_list)}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in [1, 2, 3]:
                return n


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    else:
        return randint(100, 999)


if __name__ == "__main__":
    main()

