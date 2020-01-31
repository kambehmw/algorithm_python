def dfs(num, v):
    if num == N:
        return v == 0
    for i in range(K):
        if dfs(num + 1, v ^ T[num][i]):
            return True
    return False


N, K = map(int, input().split())
T = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    T.append(tmp)

if dfs(0, 0):
    print("Found")
else:
    print("Nothing")