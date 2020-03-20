N, R = map(int, input().split())
S = input()
X = [False] * N
last = None
for i in range(N):
    if S[i] == "o":
        X[i] = True
    else:
        last = i
ans = 0
i = 0
while not all(X):
    if X[i] == False:
        ans += 1
        for j in range(i, i + R):
            X[j] = True
    elif last <= i + R - 1:
        ans += 1
        break
    else:
        i += 1
        ans += 1
print(ans)