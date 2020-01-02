def solution(N):
    ans = float('inf')
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans = min(ans, 2 * (i + N // i))
    # print(ans)
    return ans


if __name__ == '__main__':
    print(solution(30))
    print(solution(100))
