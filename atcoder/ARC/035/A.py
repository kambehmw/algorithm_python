s = input()
rev_s = reversed(s)
for c1, c2 in zip(s, rev_s):
    if c1 == "*" or c2 == "*":
        continue
    elif c1 == c2:
        continue
    else:
        print("NO")
        exit()
print("YES")