def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    answer = 0
    total_sum = 0

    r = 0
    for i in range(N):
        while total_sum < K:
            if r == N:
                break
            else:
                total_sum += A[r]
                r += 1
        if total_sum < K:
            break
        answer = answer + N - r + 1
        total_sum -= A[i]
    print(answer)


if __name__ == '__main__':
    main()