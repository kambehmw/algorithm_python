def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = set(table)
    return table

def main():
    A, B, K = list(map(int, input().split()))

    divisors = divisor(A).intersection(divisor(B))
    divisors = sorted(divisors)[::-1]
    print(divisors[K-1])

if __name__ == '__main__':
    main()