N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
cost1 = 0
for i in range(X, 0, -1):
    if i in A:
        cost1 += 1
cost2 = 0
for i in range(X, N):
    if i in A:
        cost2 += 1
print(min(cost1, cost2))