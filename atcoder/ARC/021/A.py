A = []
for _ in range(4):
    A.append([int(x) for x in input().split()])
flag = False
for y in range(4):
    for x in range(3):
        if A[y][x] == A[y][x+1]:
            flag = True

for x in range(4):
    for y in range(3):
        if A[y][x] == A[y+1][x]:
            flag = True
if flag:
    print("CONTINUE")
else:
    print("GAMEOVER")