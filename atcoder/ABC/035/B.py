S = input()
T = int(input())
x, y = 0, 0
k = 0
for s in S:
    if s == "L":
        x -= 1
    elif s == "R":
        x += 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    elif s == "?":
        k += 1

if T == 1:
    print(abs(x) + abs(y) + k)
elif T == 2:
    print(max(abs(len(S)) % 2, abs(x) + abs(y) - k))
