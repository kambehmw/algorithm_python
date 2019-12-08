def solution(X, A):
    # write your code in Python 3.6
    s = set()
    for i, a in enumerate(A):
        s.add(a)
        if len(s) == X:
            return i
    return -1

if __name__ == '__main__':
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    print(solution(X, A))