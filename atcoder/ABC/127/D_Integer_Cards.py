import heapq

N, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
BC = []
for _ in range(M):
    BC.append(tuple(map(int, input().split())))

BC.sort(key=lambda x: x[1], reverse=True)
heapq.heapify(A)
for (b, c) in BC:
    for _ in range(b):
        min_val = A[0]
        if min_val < c:
            heapq.heappop(A)
            heapq.heappush(A, c)
        else:
            break
print(sum(A))