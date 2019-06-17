def main():
    N = int(input())
    R = []
    for _ in range(N):
        R.append(int(input()))

    maxv = float("-inf")
    minv = R[0]
    for i in range(1, N):
        maxv = max(maxv, R[i] - minv)
        minv = min(minv, R[i])

    print(maxv)

if __name__ == '__main__':
    main()