N, T = map(int, input().split())
AB = []
for _ in range(N):
    a, b = map(int, input().split())
    AB.append((a, b))

B = [ab[1] for ab in AB]
if T < sum(B):
    print(-1)
    exit()

AB.sort(reverse=True, key=lambda x: x[0] - x[1])
# print(AB)
total = sum([ab[0] for ab in AB])
if total <= T:
    print(0)
else:
    for i in range(N):
        total -= AB[i][0] - AB[i][1]
        if total <= T:
            print(i + 1)
            break