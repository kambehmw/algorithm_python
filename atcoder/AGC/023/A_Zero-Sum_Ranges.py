from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom


from collections import Counter
N = int(input())
A = list(map(int, input().split()))
partial_sum = [0] * (N + 1)
partial_sum[1] = A[0]
for i in range(1, N+1):
    partial_sum[i] = partial_sum[i-1] + A[i-1]
partial_sum.sort()
counter = Counter(partial_sum)
ans = 0
for k, v in counter.items():
    if 2 <= v:
        ans += combinations_count(v, 2)
print(ans)