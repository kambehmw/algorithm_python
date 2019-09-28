N = int(input())
for i in range(1, N+1):
    total = (i * (i + 1)) // 2
    if N <= total:
        for x in range(1, i+1):
            if total - N == x:
                continue
            print(x)
        break