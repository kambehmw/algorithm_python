from collections import defaultdict
N, M = map(int, input().split())
if N == 1:
    print(0)
    exit()

d = defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split())
    d[a].add(b)
    d[b].add(a)

for i in range(1, N+1):
    tmp = set()
    for x in d[i]:
        for y in d[x]:
            if y != i and y not in d[i]:
                tmp.add(y)
    print(len(tmp))