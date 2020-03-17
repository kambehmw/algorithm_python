s = input()
st = set(s)
ans = ""
for c in st:
    ans += (c + c)
print(ans)