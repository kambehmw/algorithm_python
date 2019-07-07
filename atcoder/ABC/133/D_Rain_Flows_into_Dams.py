def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = sum(A)
    X1 = S - 2 * sum([a for i, a in enumerate(A, 1) if i >= 2 and i % 2 == 0])
    res = []
    res.append(X1)
    for i in range(0, N-1):
        X_new = 2 * A[i] - res[i]
        res.append(X_new)

    print(" ".join([str(x) for x in res]))


if __name__ == '__main__':
    main()