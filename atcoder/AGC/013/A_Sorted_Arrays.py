N = int(input())
A = list(map(int, input().split()))
flag = None
ans = 0
for i in range(N-1):
    if flag is None:
        if A[i] < A[i+1]:
            flag = True
        elif A[i+1] < A[i]:
            flag = False
        continue
    if flag:
        if A[i+1] < A[i]:
            ans += 1
            flag = None
    elif not flag:
        if A[i] < A[i+1]:
            ans += 1
            flag = None
ans += 1
print(ans)
