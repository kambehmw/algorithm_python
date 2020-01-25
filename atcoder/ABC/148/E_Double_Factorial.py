N = int(input())
if N % 2 != 0:
    print(0)
    exit()
cnt = 0
i = 0
while (5 ** i * 10) <= N:
    div = N // (5 ** i * 10)
    cnt += div
    i += 1
print(cnt)