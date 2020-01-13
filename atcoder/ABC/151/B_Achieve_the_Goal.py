N, K, M = tuple(map(int, input().split()))
A = list(map(int, input().split()))
total = sum(A)
for k in range(0, K+1):
    if M <= (total + k) // N:
        print(k)
        exit()
print(-1)