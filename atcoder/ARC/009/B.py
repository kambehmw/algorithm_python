B = list(input().split())
N = int(input())
A = [input() for _ in range(N)]
X = []
for i, a in enumerate(A):
    tmp = ""
    for c in a:
        tmp += str(B.index(c))
    X.append((int(tmp), i))
X.sort()
for x in X:
    print(A[x[1]])