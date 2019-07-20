N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
A.append(0)
S = sum([abs(A[i] - A[i+1]) for i in range(0, N+1)])
for i in range(1, N+1):
    ans = S + abs(A[i-1] - A[i+1]) - (abs(A[i-1] - A[i]) + abs(A[i] - A[i+1]))
    print(ans)