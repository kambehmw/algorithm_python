N = int(input())
A = list(map(int, input().split()))
ans = float('inf')
X = sum(A)
partial_sum = 0
for i in range(N-1):
    partial_sum += A[i]
    ans = min(ans, abs(X - 2 * partial_sum))
print(ans)
