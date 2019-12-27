S = input()
ans = 0
for s, t in zip(S, S[::-1]):
    if s != t:
       ans += 1
print(ans // 2)
