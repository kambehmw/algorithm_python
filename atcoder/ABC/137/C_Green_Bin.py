from math import factorial

def comb(n, r):
    if n == 1:
        return 0
    return factorial(n) // factorial(r) // factorial(n - r)

N = int(input())
S = [input() for _ in range(N)]
str_dict = {}
for s in S:
    sorted_s = "".join(sorted(s))
    if sorted_s not in str_dict:
        str_dict[sorted_s] = 0
    str_dict[sorted_s] += 1
ans = sum([comb(v, 2) for v in str_dict.values()])
print(int(ans))