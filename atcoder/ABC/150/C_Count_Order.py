import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
for i, x in enumerate(itertools.permutations(range(1, N+1))):
    if x == P:
        p_idx = i
    if x == Q:
        q_idx = i
print(abs(p_idx - q_idx))
