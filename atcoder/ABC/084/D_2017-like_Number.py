import math

is_primes = [False] * (10 ** 5 + 1)
def is_prime(n):
    if n == 1: return False
    if is_primes[n]:
        return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    is_primes[n] = True
    return True


Q = int(input())
total = [0] * (10 ** 5 + 1)
for i in range(1, 10**5+1):
    if is_prime(i) and is_prime((i + 1) // 2):
        total[i] = total[i-1] + 1
    else:
        total[i] = total[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    print(total[r] - total[l-1])