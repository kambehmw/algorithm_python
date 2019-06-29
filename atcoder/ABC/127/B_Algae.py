def main():
    r, D, x = list(map(int, input().split()))

    x_old = x
    for i in range(10):
        x_new = r * x_old - D
        print(x_new)
        x_old = x_new

if __name__ == '__main__':
    main()