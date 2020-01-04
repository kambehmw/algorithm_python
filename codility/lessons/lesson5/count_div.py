def solution(A, B, K):
    return (B // K) - ((A - 1) // K)


if __name__ == '__main__':
    A, B, K = 6, 11, 2
    print(solution(A, B, K))