N, Q = map(int, input().split())
counter = [0] * (N+1)
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    counter[l] += 1
    counter[r+1] -= 1

for i in range(N-1):
    counter[i+1] += counter[i]

ans = ""
for i in range(N):
    if counter[i] % 2 == 0:
        ans += "0"
    else:
        ans += "1"
print(ans)