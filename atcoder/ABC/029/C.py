import itertools
N = int(input())
for v in itertools.product(["a", "b", "c"], repeat=N):
    print("".join(v))
