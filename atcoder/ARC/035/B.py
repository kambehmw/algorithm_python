from collections import Counter
import math
N = int(input())
T = [int(input()) for _ in range(N)]
mod = 10 ** 9 + 7
T.sort()
counter = Counter(T)
time = 0
penalty = 0
for t in T:
    time += t
    penalty += time
print(penalty)
cnt = 1
for k, v in counter.items():
    cnt *= math.factorial(v) % mod
print(cnt % mod)