amount_due = 50
while amount_due > 0:
    print("Amount Due:", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due -= coin

changed_owed = abs(amount_due)
print("Changed Owed:", changed_owed)