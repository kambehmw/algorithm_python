N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]
if 0 in set(s):
    print(N)
    exit()
front, back = 0, 0
res = 1
ans = 0
while back < N and back <= front:
    if front < N and res * s[front] <= K:
        res *= s[front]
        front += 1
    else:
        ans = max(ans, front - back)
        res = res // s[back]
        back += 1
print(ans)