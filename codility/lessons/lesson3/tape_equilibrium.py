def solution(A):
    # write your code in Python 3.6
    total = sum(A)
    left_sum = 0
    ans = float('inf')
    for i in range(len(A)-1):
        left_sum += A[i]
        right_sum = total - left_sum
        ans = min(ans, abs(right_sum - left_sum))
    return ans


if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print(solution(A))