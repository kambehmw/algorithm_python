from collections import defaultdict

def solution(A):
    if len(A) == 0:
        return 0

    return len(set(A))


if __name__ == '__main__':
    A = [2, 1, 1, 2, 3, 1]
    print(solution(A))