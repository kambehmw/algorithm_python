import math
N, H = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
max_a = max(A)
B_filtered = [b for b in B if b > max_a]
B_filtered.sort(reverse=True)
cnt = 0
for b in B_filtered:
    H -= b
    cnt += 1
    if H <= 0:
        break
if 0 < H:
    cnt += math.ceil(H / max_a)
print(cnt)