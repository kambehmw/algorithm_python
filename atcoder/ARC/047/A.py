N, L = map(int, input().split())
S = input()
cnt = 1
ans = 0
for s in S:
    if s == "+":
        cnt += 1
    elif s == "-":
        cnt -= 1

    if L < cnt:
        ans += 1
        cnt = 1
print(ans)