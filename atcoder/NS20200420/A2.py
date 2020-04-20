s = input()
sr = s[::-1]
for c1, c2 in zip(s, sr):
    if c1 == c2 or (c1 == "*" or c2 == "*"):
        continue
    else:
        print("NO")
        exit()
print("YES")
