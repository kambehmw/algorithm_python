H, W = list(map(int, input().split()))
N = int(input())
A = list(map(int, input().split()))
A_val = []
for idx, a in enumerate(A, 1):
    for i in range(a):
        A_val.append(str(idx))
res = [["" for w in range(W)] for h in range(H)]
for h in range(H):
    flag = False
    if h % 2 == 0:
        flag = True
    for w in range(W):
        idx = h * W + w
        res[h][w] = A_val[idx]
    if not flag:
        res[h] = res[h][::-1]
res = ["".join(x) for x in res]
res = "\n".join(res)
print(res)

