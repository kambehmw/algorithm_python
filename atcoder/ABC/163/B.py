N, M = map(int, input().split())
A = list(map(int, input().split()))
if N < sum(A):
    print(-1)
    exit()

print(N - sum(A))