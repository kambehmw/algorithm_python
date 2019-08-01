N, K = map(int, input().split())
A = list(map(int, input().split()))
len_arr = len(A)
i = 0
ans = 0
while True:
    if i == 0:
        len_arr -= K
    else:
        len_arr -= (K - 1)
    i += 1
    ans += 1
    if len_arr <= 0:
        break
print(ans)
