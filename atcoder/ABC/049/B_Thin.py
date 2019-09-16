H, W = tuple(map(int, input().split()))
C = []
for h in range(H):
    C.append([c for c in input()])
res = [["." for _ in range(W)] for _ in range(2*H)]
diff = 0
for h in range(H):
    for w in range(W):
        if C[h][w] == "*":
            res[h+diff][w] = "*"
            res[h+diff+1][w] = "*"
    diff += 1
res = ["".join(x) for x in res]
res = "\n".join(res)
print(res)