N = int(input())
A = list(map(int, input().split()))
max_abs_diff = 0
for i in range(N-1):
    for j in range(i+1, N):
        abs_diff = abs(A[i]- A[j])
        if max_abs_diff < abs_diff:
            max_abs_diff = abs_diff
print(max_abs_diff)