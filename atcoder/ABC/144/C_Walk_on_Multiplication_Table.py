N = int(input())
min_val = float('inf')
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        min_val = min(min_val, i + N // i - 2)
print(min_val)
