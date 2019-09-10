S = input()
ans = 0
for i in range(len(S)):
    up_floors = len(S) - (i + 1)
    if S[i] == "U":
        ans += (up_floors * 1)
        ans += (i * 2)
    else:
        ans += (up_floors * 2)
        ans += i
print(ans)