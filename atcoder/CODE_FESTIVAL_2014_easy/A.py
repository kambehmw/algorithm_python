n = int(input())
A = list(map(int, input().split()))
total = 0
for i in range(n-1):
    total += A[i + 1] - A[i]
print(total / (n - 1))