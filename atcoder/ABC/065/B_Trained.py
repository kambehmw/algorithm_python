N = int(input())
A = [int(input()) for _ in range(N)]
i = 0
count = 0
while A[i] != 2:
    i = A[i] - 1
    count += 1
    if count >= N:
        print("-1")
        exit()
count += 1
print(count)