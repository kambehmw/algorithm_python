N = int(input())
ans = [0] * 6
for _ in range(N):
    MT, mT = map(float, input().split())
    if 35 <= MT:
        ans[0] += 1
    if 30 <= MT < 35:
        ans[1] += 1
    if 25 <= MT < 30:
        ans[2] += 1
    if 25 <= mT:
        ans[3] += 1
    if mT < 0 and 0 <= MT:
        ans[4] += 1
    if MT < 0:
        ans[5] += 1
print(*ans)