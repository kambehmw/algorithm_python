N = int(input())
cij = [[0 for _ in range(10)] for _ in range(10)]
for i in range(1, N+1):
    A = str(i)
    cij[int(A[0])][int(A[-1])] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += cij[i][j] * cij[j][i]
print(ans)