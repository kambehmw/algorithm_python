S = input().split()
ans = []
for s in S:
    if s == "Left":
       ans.append("<")
    elif s == "Right":
        ans.append(">")
    elif s == "AtCoder":
        ans.append("A")
print(" ".join(ans))
