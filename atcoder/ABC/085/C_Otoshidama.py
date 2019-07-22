N, Y = map(int, input().split())
for i in range(N+1):
    for j in range(0, N-i+1):
        k = N - i - j
        total_momey = 10000 * i + 5000 * j + 1000 * k
        if total_momey == Y:
            print("{} {} {}".format(i, j, k))
            exit()
print("-1 -1 -1")