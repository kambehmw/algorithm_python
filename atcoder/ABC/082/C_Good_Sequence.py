from collections import Counter
N = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
count = 0
for k, v in counter.items():
    if k < v:
        count += (v - k)
    elif v < k:
        count += v
print(count)