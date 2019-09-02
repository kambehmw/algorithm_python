K, X = map(int, input().split())
stones = [x for x in range(-1000000, 1000001)]
index_X = stones.index(X)
print(*stones[index_X-K+1:index_X+K])