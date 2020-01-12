import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

n = int(input())
A = [int(input()) for _ in range(n)]
cnt = 0
for a in A:
    if is_prime(a):
        cnt += 1
print(cnt)