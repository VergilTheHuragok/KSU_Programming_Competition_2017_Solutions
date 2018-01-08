numerals = "IVXLCDM"
numbers = [1, 5, 10, 50, 100, 500, 1000]

string = input("NUMERALS: ")

ind = 0
total = 0
skip = False
for i in string:
    if skip:
        ind += 1
        skip = False
        continue
    if ind + 1 < len(string) and numerals.index(string[ind + 1]) > numerals.index(i):
        total += numbers[numerals.index(string[ind + 1])] - numbers[numerals.index(i)]
        skip = True
    else:
        total += numbers[numerals.index(i)]
    ind += 1
print(total)