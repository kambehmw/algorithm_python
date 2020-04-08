n, c = map(int, input().split())
A = [int(input()) for _ in range(n)]
ans = float('inf')
for c1 in range(1, 11):
    for c2 in range(1, 11):
        if c1 == c2:
            continue
        cost = 0
        for i, a in enumerate(A):
            if i % 2 == 0:
                if c1 != a:
                    cost += c
            else:
                if c2 != a:
                    cost += c
        ans = min(ans, cost)
print(ans)