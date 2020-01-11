N = int(input())
A = list(map(int, input().split()))
total = sum(A)
left_sum = 0
ans = float('inf')
for i in range(N):
    left_sum += A[i]
    right_sum = total - left_sum
    ans = min(ans, abs(left_sum - right_sum))
print(ans)