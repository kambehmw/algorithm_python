import heapq
X, Y, A, B, C = map(int, input().split())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
R = list(map(int, input().split()))
P.sort(reverse=True)
Q.sort(reverse=True)
R.sort(reverse=True)
PQ = P[:X] + Q[:Y]
heapq.heapify(PQ)
i = 0
for r in R:
    if PQ[0] < r:
        heapq.heappop(PQ)
        heapq.heappush(PQ, r)
        i += 1
        if i == (X + Y):
            break
print(sum(PQ))
