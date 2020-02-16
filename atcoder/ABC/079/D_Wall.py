H, W = map(int, input().split())
C = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j, c in enumerate(input().split()):
        C[i][j] = int(c)
for k in range(10):
    for i in range(10):
        for j in range(10):
            if C[i][j] > C[i][k] + C[k][j]:
                C[i][j] = C[i][k] + C[k][j]

ans = 0
for i in range(H):
    for A in input().split():
        A = int(A)
        if A >= 0:
            ans += C[A][1]
# print(C)
print(ans)
