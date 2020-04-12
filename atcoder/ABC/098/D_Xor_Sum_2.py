N = int(input())
A = list(map(int, input().split()))
res = 0
right = 0
total = 0
for left in range(N):
    while right < N and (total ^ A[right]) == (total + A[right]):
        total += A[right]
        right += 1
    res += right - left
    if right == left:
        right += 1
    else:
        total -= A[left]
print(res)