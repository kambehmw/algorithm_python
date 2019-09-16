N, M = tuple(map(int, input().split()))
if N == 1 and M == 1:
    print(1)
    exit()

if N == 1:
    print(M - 2)
    exit()
if M == 1:
    print(N - 2)
    exit()

print((M - 2) * (N - 2))