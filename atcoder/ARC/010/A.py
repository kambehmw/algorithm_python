N, M, A, B = map(int, input().split())
C = [int(input()) for _ in range(M)]
for i, c in enumerate(C, 1):
    if N <= A:
        N += B

    if N < c:
        print(i)
        exit()

    N -= c
print("complete")
