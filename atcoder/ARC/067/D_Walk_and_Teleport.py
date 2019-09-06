N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))
cost = 0
for i in range(N-1):
    dist = X[i+1] - X[i]
    if dist * A < B:
        cost += (dist * A)
    else:
        cost += B
print(cost)