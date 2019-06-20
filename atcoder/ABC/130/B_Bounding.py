def main():
    inputs = input().split()
    N, X = int(inputs[0]), int(inputs[1])
    L = list(map(int, input().split()))

    D_old = 0.0
    count = 1
    for l in L:
        D = D_old + l
        if D <= X:
            count += 1
        D_old = D
    print(count)

if __name__ == '__main__':
    main()