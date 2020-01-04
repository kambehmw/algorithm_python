def solution(A, B):
    max_val = -1
    cnt = 0
    for a, b in zip(A, B):
        if max_val < a:
            max_val = b
            cnt += 1
    return cnt


if __name__ == '__main__':
    A = [1, 3, 7, 9, 9]
    B = [5, 6, 8, 9, 10]
    print(solution(A, B))