N = int(input())
A = [int(input()) for _ in range(N)]
for i in range(N-1):
    if A[i + 1] == A[i]:
        print("stay")
    elif A[i + 1] < A[i]:
        print("down {}".format(A[i] - A[i + 1]))
    else:
        print("up {}".format(A[i + 1] - A[i]))
