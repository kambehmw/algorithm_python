N = int(input())
colors = [int(input()) for _ in range(N)]
if len(set(colors)) == 1:
    print(-1)
    exit()

res = 0
colors = colors + colors
# print(colors)
prev = colors[0]
cnt = 1
for i in range(1, 2 * N):
    if prev == colors[i]:
       cnt += 1
    else:
        res = max(res, cnt)
        cnt = 1
        prev = colors[i]
res = max(res, cnt)
print((res - 1) // 2 + 1)