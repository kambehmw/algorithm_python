N, x = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)
CA = [a for a in A]
for i in range(N):
    total = CA[i] + CA[i+1]
    if x < total:
        if CA[i + 1] <= (total - x):
            rest = total - x - CA[i + 1]
            CA[i + 1] = 0
            CA[i] -= rest
        else:
            CA[i + 1] -= total - x


cnt = 0
for a, ca in zip(A, CA):
    cnt += (a - ca)
print(cnt)
