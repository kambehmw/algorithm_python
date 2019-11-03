import itertools
N = int(input())
d = list(map(int, input().split()))
ans = sum([x * y for x, y in itertools.combinations(d, 2)])
print(ans)