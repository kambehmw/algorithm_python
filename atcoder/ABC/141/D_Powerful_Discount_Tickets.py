import heapq

N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
A = list(map(lambda x: x*(-1), A))
heapq.heapify(A)
for i in range(M):
    tmp = heapq.heappop(A) * (-1) // 2
    heapq.heappush(A, tmp * (-1))
print(sum(A) * (-1))