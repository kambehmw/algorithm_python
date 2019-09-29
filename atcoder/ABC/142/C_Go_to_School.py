N = int(input())
A = list(map(int, input().split()))
res = [0] * N
for i, a in enumerate(A, 1):
    res[a-1] = i
print(*res)
