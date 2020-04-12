def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


K = int(input())
tot = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        x = gcd(a, b)
        for c in range(1, K+1):
            y = gcd(x, c)
            tot += y
print(tot)