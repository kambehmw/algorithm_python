N = int(input())
ST = []
for _ in range(N):
    x, l = map(int, input().split())
    ST.append((x - l, x + l))
ST.sort(key=lambda x: x[1])
# print(ST)
cur = float('-inf')
cnt = 0
for i in range(N):
    if cur <= ST[i][0]:
        cnt += 1
        cur = ST[i][1]
print(cnt)