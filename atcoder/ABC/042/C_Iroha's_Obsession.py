N, K = tuple(map(int, input().split()))
D = list(map(int, input().split()))
set_D = set(D)
i = N
while True:
    tmp_set = set([int(c) for c in str(i)])
    if len(set_D.intersection(tmp_set)) > 0:
        i += 1
        continue
    else:
        break
print(i)
