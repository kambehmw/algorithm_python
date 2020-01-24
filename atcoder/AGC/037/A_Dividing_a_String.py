S = input()
ans = ["-1"]
t = ""
for c in S:
    t += c
    if t != ans[-1]:
        ans.append(t)
        t = ""
print(len(ans)-1)