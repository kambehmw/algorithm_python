N = int(input())
A = list(map(int, input().split()))
l, r = 0, 0
ans = 0
while l < N:
    while r + 1 < N and A[r] < A[r+1]:
        r += 1
    if l <= r:
        ans = ans + (r - l + 1)
    else:
        ans += 1
    l += 1
    if r < l:
        r = l
print(ans)