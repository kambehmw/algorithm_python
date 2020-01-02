# def solution(A):
#     N = len(A)
#     if N == 0:
#         return 0
#
#     min_val = A[0]
#     diff = float('-inf')
#     for i in range(N-1):
#         if A[i+1] < A[i]:
#             if A[i+1] < min_val:
#                 min_val = A[i+1]
#         diff = max(diff, A[i+1] - min_val)
#     return diff


def solution(A):
    N = len(A)
    if N == 0:
        return 0

    min_val = A[0]
    diff = float('-inf')
    for i in range(N):
        if A[i] < min_val:
            min_val = A[i]
        diff = max(diff, A[i] - min_val)
    return diff


if __name__ == '__main__':
    A = [23171, 21011, 21123, 21366, 21013, 21367]
    print(solution(A))
