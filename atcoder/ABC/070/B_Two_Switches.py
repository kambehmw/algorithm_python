A, B, C, D = list(map(int, input().split()))
lower = max(A, C)
upper = min(B, D)
print(max(0, upper - lower))