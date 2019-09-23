import math
N, M = tuple(map(int, input().split()))
if N == M:
    print(2 * math.factorial(N) * math.factorial(M) % (10**9 + 7))
    exit()

if abs(N - M) == 1:
    print(math.factorial(N) * math.factorial(M) % (10**9 + 7))
else:
    print(0)