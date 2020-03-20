A = input()
N = len(A)
if N == 1:
    print(0)
    exit()
cnt = 0
for i in range(N // 2):
    if A[i] != A[N - 1 - i]:
        cnt += 1
if cnt == 0:
    if N % 2 == 0:
        print(25 * N)
    else:
        print(25 * (N - 1))
elif cnt == 1:
    print(25 * (N - 2) + 48)
else:
    print(25 * N)
