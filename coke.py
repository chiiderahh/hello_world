amount_due = 50

while amount_due > 0:
    print("Amount due: ", amount_due)

    coin = int(input("insert coin: "))

    if coin in [25, 10, 5]:
        amount_due -= coin

change_owed = abs(amount_due)
print("change Owed: ", change_owed)
