N = int(input())
P = list(map(int, input().split()))
min_val = P[0]
cnt = 1
for p in P[1:]:
    if min_val >= p:
        cnt += 1
    min_val = min(min_val, p)
print(cnt)