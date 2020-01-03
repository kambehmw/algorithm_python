def solution(A):
    result = set()
    for a in A:
        if abs(a) not in result:
            result.add(abs(a))
    return len(result)


if __name__ == '__main__':
    A = [-5, -3, -1, 0, 3, 6]
    print(solution(A))