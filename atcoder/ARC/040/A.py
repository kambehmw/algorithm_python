N = int(input())
S = [input() for _ in range(N)]
red = 0
blue = 0
for s in S:
    for c in s:
        if c == "R":
            red += 1
        elif c == "B":
            blue += 1
if red < blue:
    print("AOKI")
elif blue < red:
    print("TAKAHASHI")
else:
    print("DRAW")