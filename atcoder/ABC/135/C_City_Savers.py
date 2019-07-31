N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
for i, b in enumerate(B):
    if A[i] >= b:
        ans += b
    else:
        ans += A[i]
        diff = b - A[i]
        if A[i+1] >= diff:
            ans += diff
            A[i+1] -= diff
        else:
            ans += max(A[i+1], 0)
            A[i+1] = 0
print(ans)