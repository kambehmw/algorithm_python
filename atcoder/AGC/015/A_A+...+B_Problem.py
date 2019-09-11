N, A, B = list(map(int, input().split()))
if A == B:
    print(1)
    exit()
if B < A:
    print(0)
    exit()

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)
    exit()

min_val = (N - 1) * A + B
max_val = (N - 1) * B + A
print(max_val - min_val + 1)