A, B, C, K = map(int, input().split())
ans = 0
if A < K:
    K -= A
    ans += A
else:
    ans += K
    print(ans)
    exit()

if B < K:
    K -= B
else:
    print(ans)
    exit()

if C < K:
    K -= C
    ans -= C
else:
    ans -= K
print(ans)