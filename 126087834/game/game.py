import random
while True:
    try:
        n = int(input("Level: "))
        rnum = random.randint(1, n)
        guess = int(input("Guess: "))
        if guess < rnum:
            print("Too small!")
            continue
        elif guess > rnum:
            print("Too Large!")
            continue
        else:
            print("Just right!")
    except ValueError:
        continue
    break

