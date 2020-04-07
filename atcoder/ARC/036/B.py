N = int(input())
H = [int(input()) for _ in range(N)]
s, t, u = 0, 0, 0
now = True
ans = 0
for i in range(N-1):
    if H[i] < H[i + 1]:
        if now:
            t += 1
            u += 1
        else:
            # print(s, t, u)
            ans = max(ans, u - s + 1)
            s = u
            u = s + 1
            t = s + 1
            now = True
    else:
        if now:
            now = False
        u += 1
ans = max(ans, u - s + 1)
print(ans)
