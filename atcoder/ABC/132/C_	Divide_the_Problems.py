def main():
    N = int(input())
    d = list(map(int, input().split()))

    d = sorted(d)
    middle = len(d) // 2
    print(d[middle] - d[middle-1])

if __name__ == '__main__':
    main()