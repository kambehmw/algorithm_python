def solution(A):
    # write your code in Python 3.6
    d = {i: 0 for i in range(1, len(A)+1)}
    for a in A:
        if a not in d:
            return 0
        else:
            d[a] += 1
    for v in d.values():
        if v != 1:
            return 0
    return 1


if __name__ == '__main__':
    A = [4, 1, 3, 2]
    print(solution(A))