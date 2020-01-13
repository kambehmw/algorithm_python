N = int(input())
A = [int(input())for _ in range(N)]
A.sort()
max_val = A[-1]
for a in A[::-1]:
    if a != max_val:
        print(a)
        exit()