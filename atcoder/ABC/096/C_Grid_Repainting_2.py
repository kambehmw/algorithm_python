H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            continue
        count = 0
        for xs, ys in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if i + ys < 0 or i + ys >= H or j + xs < 0 or j + xs >= W:
                break
            pos_x = j + xs
            pos_y = i + ys
            if S[i][j] == "#" and S[pos_y][pos_x] == ".":
                count += 1
        if count == 4:
            print("No")
            exit()
print("Yes")