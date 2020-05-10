T = int(input())
S = [input() for _ in range(T)]
for s in S:
    st = set(s)
    if len(st) == 1:
        print(s)
    else:
        print("10" * len(s))