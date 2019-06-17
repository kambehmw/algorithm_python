def bubble_sort(A):
    exchange_count = 0
    flag = True
    while flag:
        flag = False
        for j in range(len(A)-1, 0, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
                exchange_count += 1
    return exchange_count


def main():
    N = int(input())
    A = list(map(int, input().split()))

    exchange_count = bubble_sort(A)
    print(A)
    print(exchange_count)


if __name__ == '__main__':
    main()