N, M = map(int, input().split())
for z in range(10 ** 5 + 1):
    y = M - 2 * N - 2 * z
    x = 3 * N - M + z
    if x < 0 or y < 0:
        continue
    if 0 < x or 0 < y or 0 < z:
        print(x, y, z)
        exit()
print(-1, -1, -1)