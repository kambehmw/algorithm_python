def solution(A):
    N = len(A)
    A.sort()
    result = 0
    for x in range(N):
        z = x + 2
        for y in range(x+1, N):
            while z < N and A[x] + A[y] > A[z]:
                z += 1
            result += z - y - 1
    return result


if __name__ == '__main__':
    A = [10, 2, 5, 1, 8, 12]
    print(solution(A))

