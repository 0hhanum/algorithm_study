import sys

price, zero = sys.stdin.readline().split()

zero = int(zero)
if zero == 0 or price == "0":
    print(price)
elif len(str(price)) < zero:
    print("0")
elif len(str(price)) == zero:
    price = str(price)
    if price[0] < "5":
        print("0")
    else:
        print("1" + "0" * zero)

else:
    target = int(price[-zero])
    if target >= 5:
        price = str(int(price[:-zero]) + 1) + "0" * zero

    else:
        price = price[:-zero] + "0" * zero
    print(price)
