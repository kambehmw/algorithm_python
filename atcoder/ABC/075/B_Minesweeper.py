import pprint
H, W = list(map(int, input().split()))
S = []
for h in range(H):
    S.append([c for c in input()])
# pprint.pprint(S)
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            count = 0
            for pos_y in [-1, 0, 1]:
                for pos_x in [-1, 0, 1]:
                    y = h + pos_y
                    x = w + pos_x
                    if x < 0 or x >= W or y < 0 or y >= H:
                        continue
                    if S[y][x] == "#":
                        count += 1
            S[h][w] = str(count)
# pprint.pprint(S)
S = ["".join(s) for s in S]
S = "\n".join(S)
print(S)