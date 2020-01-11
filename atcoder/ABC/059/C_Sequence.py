n = int(input())
arr = [0] + list(map(int, input().split()))
cnt = 0
ans = float('inf')
for sign in [-1, 1]:
    res = 0
    partial_sum = 0
    A = [x for x in arr]
    for i in range(n):
        partial_sum += A[i]
        diff = sign - (partial_sum + A[i+1]                )
        if sign < 0:
            diff = min(diff, 0)
        else:
            diff = max(diff, 0)
        res += abs(diff)
        A[i+1] += diff
        sign *= -1
    ans = min(ans, res)
print(ans)
