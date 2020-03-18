import heapq
from collections import defaultdict
N, M = map(int, input().split())
AB = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    AB[a].append(b)
# print(AB)
h = []
ans = 0
for i in range(1, M+1):
    if i in AB:
        for x in AB[i]:
            heapq.heappush(h, - x)
    if len(h) > 0:
        ans -= heapq.heappop(h)
print(ans)