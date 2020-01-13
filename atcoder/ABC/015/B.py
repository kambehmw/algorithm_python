import math
N = int(input())
A = list(map(int, input().split()))
total, cnt = 0, 0
for a in A:
    if a != 0:
        total += a
        cnt += 1
print(math.ceil(total / cnt))