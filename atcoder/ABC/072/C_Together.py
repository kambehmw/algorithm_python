from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for a in A:
    d[a-1] += 1
    d[a] += 1
    d[a+1] += 1
print(max(d.values()))