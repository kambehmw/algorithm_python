S = input()
parts = S.split("+")
ans = 0
for p in parts:
    if "0" not in p:
        ans += 1
print(ans)