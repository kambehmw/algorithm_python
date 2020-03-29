R, C, D = map(int, input().split())
A = []
for _ in range(R):
    A.append([int(c) for c in input().split()])

ans = 0
for h in range(R):
    w = D - h
    while 0 <= w:
        if w < C:
            ans = max(ans, A[h][w])
        w -= 2
print(ans)
