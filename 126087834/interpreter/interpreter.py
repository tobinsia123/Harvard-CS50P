expression = input("Expression: ")
x,y,z = expression.split(" ")

x_1 = float(x)
z_1 = float(z)

if y == "+":
    print((x_1) + (z_1))
elif y == "-":
    print((x_1) - (z_1))
elif y == "*":
    print((x_1) * (z_1))
elif y == "/":
    print((x_1) / (z_1))