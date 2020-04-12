N = int(input())
K = list(map(int, input().split()))
K = [float('inf')] + K + [float('inf')]
L = []
for i in range(1, N+1):
    L.append(min(K[i], K[i - 1]))
print(*L)