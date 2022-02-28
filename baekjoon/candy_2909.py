import sys

price, zero = sys.stdin.readline().split()
zero = int(zero)
if zero == 0:
    print(price)
else:
    target = int(price[-zero])
    if target >= 5:
        price = str(int(price[:-zero]) + 1) + "0" * zero

    else:
        price = price[:-zero] + "0" * zero
    print(price)