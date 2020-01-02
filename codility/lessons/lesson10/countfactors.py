def solution(N):
    ans = set()
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            ans.add(i)
            ans.add(N // i)
    # print(ans)
    return len(ans)


if __name__ == '__main__':
    print(solution(24))
    print(solution(35))