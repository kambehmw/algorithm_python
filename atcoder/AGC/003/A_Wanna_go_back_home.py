def check(d1, d2, direction):
    if d1 in direction and not d2 in direction:
        return False
    if d2 in direction and not d1 in direction:
        return False
    return True

S = input()
direction = {s for s in S}
for (x, y) in [("N", "S"), ("W", "E")]:
    if not check(x, y, direction):
        print("No")
        exit()

print("Yes")
