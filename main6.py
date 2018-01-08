inp = [int(i) for i in input().replace(" ", "")]
non_zero = list(filter(lambda x: x != 0, inp[:]))

zeros = []
ind = 0
for num in inp:
    if num == 0:
        zeros.append(ind)
    ind += 1

min_non = sorted(non_zero[:])

moves = 0
last = []
for i in min_non:
    ind = 0
    lst = non_zero[:non_zero.index(i)]
    if len(lst) > 0:
        for i2 in lst:
            if i < i2:
                non_zero.remove(i2)
                non_zero.insert(ind, i)
                nind = non_zero.index(i, ind + 1)
                non_zero.pop(nind)
                non_zero.insert(nind, i2)
                moves += 1
                nfinal = non_zero[:]
                for zero in zeros:
                    nfinal.insert(zero, 0)
                print(nfinal)
                break
            ind += 1
print(moves)
