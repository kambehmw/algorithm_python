def solution(A):
    A.sort()
    A = [a for a in A if a > 0]
    if not A:
        return 1
    max_val = max(A)
    set_A = set(A)
    for i in range(1, max_val):
        if i not in set_A:
            return i
    return max_val + 1

if __name__ == '__main__':
    A = [1, 3, 6, 4, 1, 2]
    print(solution(A))

    A = [1, 2, 3]
    print(solution(A))

    A = [-1, -3]
    print(solution(A))