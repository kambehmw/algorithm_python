N, P = list(map(int, input().split()))
A = list(map(int, input().split()))
has_odd = False
for a in A:
    if a % 2 != 0:
        has_odd = True
        break
if not has_odd:
    if P == 0:
        print(2**N)
        exit()
    else:
        print(0)
        exit()
else:
    print(2 ** (N - 1))