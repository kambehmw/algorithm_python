N = int(input())
ans = []
for fx in range(9 * 18 + 1):
    if 0 < N - fx:
        x = N - fx
        total = 0
        for c in str(x):
            total += int(c)
        if x + total == N:
            ans.append(x)

ans.sort()
print(len(ans))
for x in ans:
    print(x)