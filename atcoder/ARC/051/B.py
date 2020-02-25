counter = 0


def gcd(a, b):
    if b == 0:
        return a
    global counter
    counter += 1
    return gcd(b, a % b)


def fib_memo(n):
    memo = ["EMPTY"] * (n + 1)

    def _fib(n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        elif memo[n] != "EMPTY":
            return memo[n]
        else:
            memo[n] = _fib(n - 1) + _fib(n - 2)
            return memo[n]

    return _fib(n)


K = int(input())
a, b = fib_memo(K + 2), fib_memo(K + 1)
# gcd(a, b)
# print(counter)
print(a, b)