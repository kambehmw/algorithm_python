def main():
    L, R = list(map(int, input().split()))
    if (R - L) >= 673:
        print(0)
    else:
        res = float('inf')
        for i in range(L, R):
            for j in range(i+1, R+1):
                res = min(res, (i * j) % 2019)
        print(res)

if __name__ == '__main__':
    main()