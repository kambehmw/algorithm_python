n = int(input())
min_val = float('inf')
for x in range(1, n+1):
    y = n // x
    min_val = min(abs(x - y) + n - x * y, min_val)
print(min_val)
