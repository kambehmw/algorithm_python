def solution(K, A):
    cnt, current = 0, 0
    for a in A:
        current += a
        if K <= current:
            cnt += 1
            current = 0
    return cnt


if __name__ == '__main__':
    K = 4
    A = [1, 2, 3, 4, 1, 1, 3]
    print(solution(K, A))