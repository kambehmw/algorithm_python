N = int(input())
colors = [int(input()) for _ in range(N)]
if len(set(colors)) == 1:
    print(-1)
    exit()

idx = None
for i in range(N-1):
    if colors[i] != colors[i + 1]:
        idx = i
        break

res = 0
colors = colors[idx+1:] + colors[:idx+1]
# print(colors)
prev = colors[0]
cnt = 1
for i in range(1, N):
    if prev == colors[i]:
       cnt += 1
    else:
        res = max(res, cnt)
        cnt = 1
        prev = colors[i]
res = max(res, cnt)
print((res - 1) // 2 + 1)