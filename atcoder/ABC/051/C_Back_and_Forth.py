sx, sy, tx, ty = tuple(map(int, input().split()))
dx = tx - sx
dy = ty - sy
ans = ""
ans += "U" * dy
ans += "R" * dx
ans += "D" * dy
ans += "L" * dx
ans += ("L" + "U" * (dy + 1) + "R" * (dx + 1) + "D")
ans += ("R" + "D" * (dy + 1) + "L" * (dx + 1) + "U")
print(ans)
