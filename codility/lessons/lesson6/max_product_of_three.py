def solution(A):
    A.sort(reverse=True)
    ans = A[0] * A[-2] * A[-1]
    for i in range(len(A)):
        ans = max(ans, A[i-2] * A[i-1] * A[i])
    return ans

if __name__ == '__main__':
    A = [-3, 1, 2, -2, 5, 6]
    print(solution(A))