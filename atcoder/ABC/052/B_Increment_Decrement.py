N = int(input())
S = input()
max_val = 0
x = 0
for s in S:
    if s == "I":
        x += 1
    else:
        x -= 1
    if max_val < x:
        max_val = x
print(max_val)