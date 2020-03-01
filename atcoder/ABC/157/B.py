A = []
for _ in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
B = [int(input()) for _ in range(N)]
bingo = [[False for _ in range(3)] for _ in range(3)]
for b in B:
    for h in range(3):
        for w in range(3):
            if A[h][w] == b:
                bingo[h][w] = True

for w in range(3):
    flag = True
    for h in range(3):
        if not bingo[h][w]:
            flag = False
            break
    if flag:
        print("Yes")
        exit()

for h in range(3):
    flag = True
    for w in range(3):
        if not bingo[h][w]:
            flag = False
            break
    if flag:
        print("Yes")
        exit()

flag = True
for i in range(3):
    if not bingo[i][i]:
        flag = False
        break

if flag:
    print("Yes")
    exit()

flag = True
for i in range(3):
    if not bingo[i][2-i]:
        flag = False
        break
if flag:
    print("Yes")
    exit()
print("No")