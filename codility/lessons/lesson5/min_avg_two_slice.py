def solution(A):
    N = len(A)
    min_avg = (A[0] + A[1]) / 2.0
    idx = 0
    for i in range(2, N):
        tmp1 = (A[i-1] + A[i]) / 2.0
        tmp2 = (A[i-2] + A[i-1] + A[i]) / 3.0
        if tmp1 < min_avg:
            min_avg = tmp1
            idx = i - 1
        if tmp2 < min_avg:
            min_avg = tmp2
            idx = i - 2
    return idx


if __name__ == '__main__':
    A = [4, 2, 2, 5, 1, 5, 8]
    print(solution(A))