def main():
    A, P = list(map(int, input().split()))

    total_ingredient = A * 3 + P
    print(total_ingredient // 2)

if __name__ == '__main__':
    main()