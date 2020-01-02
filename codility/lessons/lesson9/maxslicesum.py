def solution(A):
    if max(A) < 0:
        return max(A)

    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


if __name__ == '__main__':
    A = [3, 2, -6, 4, 0]
    print(solution(A))

    A = [-3, -2, -1]
    print(solution(A))