N = int(input())
A = [int(input()) for _ in range(N)]
A = list(set(A))
A.sort()
# print(A)
print(A[-2])