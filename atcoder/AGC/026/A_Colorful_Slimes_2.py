N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N-1):
    if A[i] == A[i+1]:
        A[i+1] = None
        ans += 1
print(ans)