N, T = tuple(map(int, input().split()))
A = [int(input()) for _ in range(N)]
total_time = 0
for i in range(N-1):
    diff = A[i+1] - A[i]
    if T <= diff:
        total_time += T
    else:
        total_time += diff
total_time += T
print(total_time)
