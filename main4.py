inp = input()

x = int(inp[0])
y = int(inp[2])

npos = []

combos = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]

for combo in combos:
    nx = x + combo[0]
    ny = y + combo[1]
    if nx <=8 and ny <= 8 and nx > 0 and ny > 0:
        npos.append([nx, ny])

print(len(npos))
for ans in npos[::-1]:
    print(ans)