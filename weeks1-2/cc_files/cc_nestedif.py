priceIsRight = 15

if priceIsRight < 5:
    print("Price is too low!")
elif 5 <= priceIsRight <= 9:
    print("Price is almost there!")
elif priceIsRight == 10:
    print("Price is exactly that!")
else:
    print("Price is too high!")