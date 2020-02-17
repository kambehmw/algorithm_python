m, n, N = map(int, input().split())
ans = N
while m <= N:
    N -= m
    N += n
    ans += n
print(ans)