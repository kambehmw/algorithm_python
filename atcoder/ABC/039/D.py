H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())
cand = [["#" for _ in range(W)] for _ in range(H)]
for h in range(H):
    for w in range(W):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                py = h + i
                px = w + j
                if py < 0 or H <= py:
                    continue
                if px < 0 or W <= px:
                    continue
                if S[py][px] == ".":
                    cand[h][w] = "."
                    break
ans = [["." for _ in range(W)] for _ in range(H)]
for h in range(H):
    for w in range(W):
        if cand[h][w] == "#":
            ans[h][w] = "#"
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    py = h + i
                    px = w + j
                    if py < 0 or H <= py:
                        continue
                    if px < 0 or W <= px:
                        continue
                    ans[py][px] = "#"
for h in range(H):
    for w in range(W):
        if S[h][w] != ans[h][w]:
            print("impossible")
            exit()
print("possible")
print("\n".join(["".join(x) for x in cand]))