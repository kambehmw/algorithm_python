N = int(input())
A = list(map(int, input().split()))
if sum(A) % N != 0:
    print(-1)
    exit()

cnt = 0
ave = sum(A) // N
total = 0
cnt = 0
ans = 0
for i, a in enumerate(A, 1):
    total += a
    cnt += 1
    if total != ave * cnt:
        ans += 1
print(ans)