def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    N = int(input())
    A = list(map(int, input().split()))

    L = [0]
    R = [0]
    for i in range(N):
        L.append(gcd(L[i], A[i]))
        R.append(gcd(R[i], A[N-i-1]))

    R.reverse()
    M = [gcd(L[i], R[i+1]) for i in range(N)]
    print(max(M))


if __name__ == '__main__':
    main()