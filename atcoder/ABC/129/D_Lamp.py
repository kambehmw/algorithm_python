H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
cnt = [[1 for _ in range(W)] for _ in range(H)]
for h in range(H):
    ws = 0
    for w in range(W):
        if S[h][w] == "#":
            ws = 0
        else:
            cnt[h][w] += ws
            ws += 1
    ws = 0
    for w in range(W-1, -1, -1):
        if S[h][w] == "#":
            ws = 0
        else:
            cnt[h][w] += ws
            ws += 1

for w in range(W):
    hs = 0
    for h in range(H):
        if S[h][w] == "#":
            hs = 0
        else:
            cnt[h][w] += hs
            hs += 1
    hs = 0
    for h in range(H-1, -1, -1):
        if S[h][w] == "#":
            hs = 0
        else:
            cnt[h][w] += hs
            hs += 1
ans = 0
for h in range(H):
    for w in range(W):
        ans = max(ans, cnt[h][w])
print(ans)

