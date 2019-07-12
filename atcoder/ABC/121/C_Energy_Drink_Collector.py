N, M = map(int, input().split())
data = []
for i in range(N):
    A, B = map(int, input().split())
    data.append((A, B))

data = sorted(data, key=lambda x: x[0])
count = 0
total = 0
for d in data:
    count += d[1]
    if count >= M:
        total += d[0] * (d[1] - (count - M))
        break
    else:
        total += d[0] * d[1]
print(total)