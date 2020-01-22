A, K = map(int, input().split())
base = 2 * 10 ** 12
if K == 0:
    print(base - A)
    exit()
cnt = 0
while A < base:
    A += (1 + K * A)
    cnt += 1
print(cnt)