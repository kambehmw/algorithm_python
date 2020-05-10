N, K = map(int, input().split())
A = list(map(int, input().split()))
s = []
d = [-1] * (N + 1)
v = 1
c, l = 1, 0
while d[v] == -1:
    d[v] = len(s)
    s.append(v)
    v = A[v - 1]
c = len(s) - d[v]
l = d[v]
if K < l:
    print(s[K])
else:
    K -= l
    K %= c
    print(s[l + K])