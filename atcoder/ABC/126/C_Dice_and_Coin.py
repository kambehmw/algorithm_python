def main():
    N, K = list(map(int, input().split()))

    total_prob = 0.0
    for i in range(1, N+1):
        res = i
        prob = 1 / N
        while res < K:
            prob *= 0.5
            res *= 2

        total_prob += prob

    print(total_prob)


if __name__ == '__main__':
    main()