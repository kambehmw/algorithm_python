import copy
import pprint
A = []
for _ in range(10):
    A.append([c for c in input()])

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x, X):
    if X[y][x] == "x":
        return

    X[y][x] = "x"
    for py, px in zip(dy, dx):
        ty = y + py
        tx = x + px
        if ty < 0 or 10 <= ty or tx < 0 or 10 <= tx:
            continue
        if X[ty][tx] == "x":
            continue

        dfs(ty, tx, X)

def check(X):
    for h in range(10):
        for w in range(10):
            if X[h][w] == "o":
                return False
    return True


sy, sx = None, None
flag = False
for h in range(10):
    for w in range(10):
        if A[h][w] == "o":
            sy, sx = h, w
            flag = True
            break
    if flag:
        break

X = copy.deepcopy(A)
dfs(sy, sx, X)
if check(X):
    print("YES")
    exit()

for h in range(10):
    for w in range(10):
        X = copy.deepcopy(A)
        if X[h][w] == "o":
            continue
        X[h][w] = "o"
        # pprint.pprint(X)
        dfs(sy, sx, X)
        # pprint.pprint(X)
        if check(X):
            # print(h, w)
            print("YES")
            exit()
print("NO")