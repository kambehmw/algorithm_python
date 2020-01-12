W, H, x, y, r = tuple(map(int, input().split()))
if x - r < 0 or x + r > W or y - r < 0 or y + r > H:
    print("No")
else:
    print("Yes")
