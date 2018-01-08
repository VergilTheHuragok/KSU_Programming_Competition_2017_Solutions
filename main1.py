x = float(input("weight: "))
y = float(input("cost: "))
x2 = float(input("weight2: "))
y2 = float(input("cost2: "))



peroz = y / x
peroz2 = y2 / x2

if min(float(peroz), float(peroz2)) == peroz:
    print("Item 1 is a better buy. Item 1 is $" + str(peroz) + " per ounce.", "Item 2 is $" + str(peroz2) + " per ounce.")
else:
    print("Item 2 is a better buy. Item 2 is $" + str(peroz2) + " per ounce.", "Item 1 is $" + str(peroz) + " per ounce.")
