from collections import Counter

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
counter = Counter()
for i in range(2, N+1):
    counter.update(Counter(prime_factorize(i)))
ans = 1
for value in counter.values():
    ans *= (value + 1)
print(ans % (10**9 + 7))