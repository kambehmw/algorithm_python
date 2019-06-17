def selection_sort(A):
    exchange_count = 0
    for i in range(0, len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j] < A[minj]:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
            exchange_count += 1
    return exchange_count

def main():
    N = int(input())
    A = list(map(int, input().split()))

    exchange_count = selection_sort(A)
    print(A)
    print(exchange_count)


if __name__ == '__main__':
    main()