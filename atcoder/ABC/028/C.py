import itertools

A, B, C, D, E = map(int, input().split())
X = list(itertools.permutations((A, B, C, D, E), 3))
X_sum = [sum(x) for x in X]
ans = sorted(set(X_sum))
print(ans[-3])