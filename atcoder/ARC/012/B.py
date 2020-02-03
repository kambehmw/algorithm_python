N, va, vb, L = map(int, input().split())
for i in range(N):
    L = vb * (L / va)
print("{:.8f}".format(L))