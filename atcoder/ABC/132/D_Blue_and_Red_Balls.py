# as this method is slow, time out error occurred
def factorial(n):
    total = 1
    for i in range(1, n+1):
        total *= i
    return total

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

MOD = 1000000000 + 7
def main():
    N, K = list(map(int, input().split()))

    for k in range(1, K+1):
        res = combinations_count(N-K+1, k)
        res *= combinations_count(K-1, k-1)
        print(res % MOD)

if __name__ == '__main__':
    main()