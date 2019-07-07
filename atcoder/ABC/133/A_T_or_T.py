def main():
    N, A, B = list(map(int, input().split()))
    print(min(A * N, B))

if __name__ == '__main__':
    main()