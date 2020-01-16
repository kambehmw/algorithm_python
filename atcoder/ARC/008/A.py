N = int(input())
if N % 10 < 7:
    print(N // 10 * 100 + 15 * (N % 10))
else:
    print((N // 10 + 1) * 100)