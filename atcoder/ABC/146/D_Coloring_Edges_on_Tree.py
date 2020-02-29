import sys

sys.setrecursionlimit(10 ** 7)

n = int(input())
A = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A[a].append([b, i])

ans = [0] * (n - 1)


def col(now, color):
    c = 1
    for (b, j) in A[now]:
        if c == color:
            c += 1
        ans[j] = c
        col(b, c)
        c += 1


col(0, 0)
print(max(ans))
for a in ans:
    print(a)
