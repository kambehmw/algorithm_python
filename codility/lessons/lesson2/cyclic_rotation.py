def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return []

    return A[-K % len(A):] + A[:-K % len(A)]

if __name__ == '__main__':
    A = [3, 8, 9, 7, 6]
    K = 3
    print(solution(A, K))