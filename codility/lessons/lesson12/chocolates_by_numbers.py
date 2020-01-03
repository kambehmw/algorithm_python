def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(N, M):
    return N // gcd(N, M)


if __name__ == '__main__':
    print(solution(10, 4))
    print(solution(12, 4))