def main():
    n = int(input())
    p = list(map(int, input().split()))

    count = 0
    for i in range(1, n - 1):
        #print(p[i-1], p[i], p[i+1])
        if min(p[i-1], p[i], p[i+1]) != p[i] and max(p[i-1], p[i], p[i+1]) != p[i]:
            count += 1

    print(count)

if __name__ == '__main__':
    main()