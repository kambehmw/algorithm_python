K, T = tuple(map(int, input().split()))
A = list(map(int, input().split()))
max_val = max(A)
print(max(max_val - 1 -(K - max_val), 0))