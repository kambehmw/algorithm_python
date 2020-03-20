N = int(input())
S = [[c for c in input()] for _ in range(N)]
W = len(S[0])
ans = 0
for h in range(N):
    for w in range(W-1, -1, -1):
        if S[h][w] == ".":
            for i in range(w, -1, -1):
                S[h][i] = "o"
            if h + 1 < N:
                for i in range(w, W):
                    S[h + 1][i] = "o"
            ans += 1
print(ans)
