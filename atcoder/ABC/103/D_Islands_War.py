N, M = map(int, input().split())
AB = []
for _ in range(M):
    a, b = map(int, input().split())
    AB.append((a, b))
AB.sort(key=lambda x: x[1])
cnt = 1
x = AB[0][1]
for a, b in AB:
    if a <= x - 1 <= b and a <= x <= b:
        continue
    else:
        cnt += 1
        x = b
print(cnt)