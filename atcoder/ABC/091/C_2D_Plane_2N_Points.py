N = int(input())
reds = [tuple(map(int, input().split())) for _ in range(N)]
blues = [tuple(map(int, input().split())) for _ in range(N)]
reds.sort(key=lambda x: x[1], reverse=True)
blues.sort(key=lambda x: x[0])
ans = 0
for b in blues:
    for i, r in enumerate(reds):
        if b[0] > r[0] and b[1] > r[1]:
            ans += 1
            del reds[i]
            break
print(ans)
