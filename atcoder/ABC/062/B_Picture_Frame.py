H, W = tuple(map(int, input().split()))
A = []
for h in range(H):
    A.append([c for c in input()])
res = [["#" for _ in range(W+2)] for _ in range(H+2)]
for i in range(1, H+1):
    for j in range(1, W+1):
        res[i][j] = A[i-1][j-1]
res = ["".join(x) for x in res]
res = "\n".join(res)
print(res)