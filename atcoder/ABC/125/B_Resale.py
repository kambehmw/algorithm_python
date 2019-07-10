def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))

    print(sum([x - y for x, y in zip(V, C) if x > y]))


if __name__ == '__main__':
    main()