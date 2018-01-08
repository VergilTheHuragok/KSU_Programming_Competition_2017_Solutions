x = input("Number: ")

answers = 0

for i in range(1, 7):
    for i2 in range(1, 7):
        for i3 in range(1, 7):
            if i + i2 + i3 == int(x):
                answers += 1
                print("(" + str(i) + ", " + str(i2) + ", " + str(i3) + ")")

print(answers)

