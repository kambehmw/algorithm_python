N = int(input())
W = [int(input()) for _ in range(N)]
X = [W[0]]
for i in range(1, N):
    flag = True
    for j, x in enumerate(X):
        if W[i] <= x:
            X[j] = W[i]
            flag = False
            break
    if flag:
        X.append(W[i])
print(len(X))