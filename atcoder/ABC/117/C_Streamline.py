N, M = map(int, input().split())
X = list(map(int, input().split()))

X = sorted(X)
diff = []
for i in range(M-1):
    diff.append(X[i+1] - X[i])
diff = sorted(diff)[::-1]
print(X[-1] - X[0] - sum(diff[:N-1]))