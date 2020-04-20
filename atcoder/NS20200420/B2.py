x, y, W = input().split()
c = []
for _ in range(9):
    c.append(input())

x, y = int(x) - 1, int(y) - 1
ans = ""
if W == "R":
    dx = 1
    for _ in range(4):
        ans += c[y][x]
        if x == 8:
            dx = -1
        x += dx
elif W == "L":
    dx = -1
    for _ in range(4):
        ans += c[y][x]
        if x == 0:
            dx = 1
        x += dx
elif W == "U":
    dy = -1
    for _ in range(4):
        ans += c[y][x]
        if y == 0:
            dy = 1
        y += dy
elif W == "D":
    dy = 1
    for _ in range(4):
        ans += c[y][x]
        if y == 8:
            dy = -1
        y += dy
elif W == "RU":
    dx, dy = 1, -1
    for _ in range(4):
        ans += c[y][x]
        if y == 0:
            dy = 1
        if x == 8:
            dx = -1
        y += dy
        x += dx
elif W == "RD":
    dx, dy = 1, 1
    for _ in range(4):
        ans += c[y][x]
        if y == 8:
            dy = -1
        if x == 8:
            dx = -1
        y += dy
        x += dx
elif W == "LU":
    dx, dy = -1, -1
    for _ in range(4):
        ans += c[y][x]
        if y == 0:
            dy = 1
        if x == 0:
            dx = 1
        y += dy
        x += dx
elif W == "LD":
    dx, dy = -1, 1
    for _ in range(4):
        ans += c[y][x]
        if y == 8:
            dy = -1
        if x == 0:
            dx = 1
        y += dy
        x += dx
print(ans)
