def main():
    N, L = list(map(int, input().split()))

    taste = [L+i-1 for i in range(1, N+1)]
    abs_taste = [abs(x) for x in taste]
    delete_index = abs_taste.index(min(abs_taste))
    taste.pop(delete_index)
    print(sum(taste))

if __name__ == '__main__':
    main()