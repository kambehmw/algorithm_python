C = []
ans = [['.' for _ in range(4)] for _ in range(4)]
for _ in range(4):
    C.append([c for c in input() if c != " "])
for h in range(4):
    for w in range(4):
        ans[3-h][3-w] = C[h][w]
for a in ans:
    print(" ".join(a))