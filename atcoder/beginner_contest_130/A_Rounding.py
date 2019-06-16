def main():
    inputs = input().split()
    X, A = int(inputs[0]), int(inputs[1])

    if X < A:
        print("0")
    else:
        print("10")


if __name__ == '__main__':
    main()