def main():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    count = 0
    for a in A:
        result = sum([x * y for x, y in zip(a, B)]) + C
        if result > 0:
            count += 1

    print(count)

if __name__ == '__main__':
    main()