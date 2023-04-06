while True:
    fuel = input("Fraction: ")
    try:
        x,y = fuel.split("/")
        x_new = int(x)
        y_new = int(y)
        f = (x_new / y_new)
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass

p = float(f * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{round(p)}%")