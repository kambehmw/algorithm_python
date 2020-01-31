import math
A, B, K, L = map(int, input().split())
set_num = K // L
print(min(set_num * B + (K - set_num * L) * A, math.ceil(K / L) * B))
