def solution(A):
    N = len(A)
    sorted_A = sorted(A)
    candidate = sorted_A[N // 2]
    count = 0
    for i in range(N):
        if sorted_A[i] == candidate:
            count += 1

    leader = -1
    if count > N // 2:
        leader = candidate

    leader_occurs = 0
    ans = 0
    for i in range(N):
        if A[i] == leader:
            leader_occurs += 1
        left_half = (i + 1) // 2
        right_half = (N - (i + 1)) // 2
        if left_half < leader_occurs and right_half < (count - leader_occurs):
            ans += 1
    return ans

if __name__ == '__main__':
    A = [4, 3, 4, 4, 4, 2]
    print(solution(A))