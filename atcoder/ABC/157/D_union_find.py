class UnionFind:
    def __init__(self, n):
        self.d = [-1] * n

    def find(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.d[x] > self.d[y]:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.d[self.find(x)]


N, M, K = map(int, input().split())
NMAX = 100005
deg = [0] * NMAX
to = [[] for _ in range(NMAX)]
uf = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    deg[a] += 1
    deg[b] += 1
    uf.unite(a, b)
for i in range(K):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    to[a].append(b)
    to[b].append(a)
anss = []
for i in range(N):
    ans = uf.size(i) - 1 - deg[i]
    for u in to[i]:
        if uf.same(i, u):
            ans -= 1
    anss.append(ans)
print(" ".join(map(str, anss)))

