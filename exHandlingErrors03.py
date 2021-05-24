
try:
    balBank = 10000
    if balBank < 15000:
        raise ValueError("You are having insufficient funds. Could you please add some money")

    else:
        print("You are eligible to purchase iphone")

except ValueError as e:
    print(e)


