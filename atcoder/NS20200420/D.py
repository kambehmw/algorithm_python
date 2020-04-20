N, M = map(int, input().split())
AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))

AB.sort(key=lambda x: x[1])
# print(AB)
base = AB[0][1]
ans = 1
for ab in AB[1:]:
    if ab[0] < base <= ab[1]:
        continue
    else:
        ans += 1
        base = ab[1]
print(ans)