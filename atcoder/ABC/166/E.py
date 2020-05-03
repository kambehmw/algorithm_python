from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
L = defaultdict(int)
R = defaultdict(int)
for i in range(N):
    L[i + A[i]] += 1
    R[i - A[i]] += 1

ans = 0
for k, v in L.items():
    ans += v * R[k]
print(ans)