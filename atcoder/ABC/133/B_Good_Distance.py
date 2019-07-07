def main():
    N, D = list(map(int, input().split()))
    X = []
    for i in range(N):
        X.append(list(map(int, input().split())))

    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            total = 0.0
            for x, y in zip(X[i], X[j]):
                total += abs(x - y) ** 2
            total = total ** 0.5
            if int(total) == total:
                count += 1

    print(count)

if __name__ == '__main__':
    main()