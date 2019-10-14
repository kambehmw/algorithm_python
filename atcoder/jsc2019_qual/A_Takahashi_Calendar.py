M, D = tuple(map(int, input().split()))
ans = 0
for m in range(M+1):
    for d in range(D+1):
        d1 = d // 10
        d10 = d % 10
        if d1 >= 2 and d10 >= 2 and d1 * d10 == m:
            ans += 1
print(ans)