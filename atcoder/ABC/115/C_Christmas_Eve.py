N, K = map(int, input().split())
H = []
for i in range(N):
    H.append(int(input()))

H = sorted(H)
min_diff = float('inf')
for i in range(0, N-K+1):
    diff = H[i+K-1] - H[i]
    if diff < min_diff:
        min_diff = diff
print(min_diff)
