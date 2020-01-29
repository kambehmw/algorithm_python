import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # nの平方根まで計算する
    m = math.floor(math.sqrt(n)) + 1
    for p in range(3, m, 2):
        if n % p == 0:
            return False
    return True

N = int(input())
if N == 1:
    print("Not Prime")
    exit()

if is_prime(N):
    print("Prime")
    exit()

d = int(str(N)[-1])
if d % 2 == 0 or d == 5:
    print("Not Prime")
    exit()

total = sum([int(s) for s in str(N)])
if total % 3 == 0:
    print("Not Prime")
    exit()

print("Prime")