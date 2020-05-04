H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append([c for c in input()])

memo = [[-1] * W for _ in range(H)]

def judge(i, j):
    if i < 0 or H <= i or j < 0 or W <= j or S[i][j] == "#":
        return 1
    if memo[i][j] != -1:
        return memo[i][j]
    res = 0
    if judge(i + 1, j) == 0:
        res = 1
    if judge(i + 1, j + 1) == 0:
        res = 1
    if judge(i, j + 1) == 0:
        res = 1
    memo[i][j] = res
    return res

ans = judge(0, 0)
if ans:
    print("First")
else:
    print("Second")