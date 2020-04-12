def solution(A):
    s = set(A)
    N = len(A)
    t = set()
    for i in range(N):
        t.add(A[i])
        if len(s) == len(t):
            return i
    return i


if __name__ == '__main__':
    A = [2, 2, 1, 0, 1]
    P = solution(A)
    print(P)