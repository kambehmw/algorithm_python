N = int(input())
MAX_N = 10 ** 6 + 5
X = [0] * (MAX_N)
for _ in range(N):
    a, b = map(int, input().split())
    X[a] += 1
    X[b + 1] -= 1
for i in range(MAX_N - 1):
    X[i + 1] += X[i]
print(max(X))
