def main():
    N = input()
    A = list(map(int, input().split()))
    count = 0
    flag = False
    while True:
        for x in A:
            if x % 2 != 0:
                flag = True

        if flag:
            print(count)
            break

        A = [x / 2 for x in A]
        count += 1

if __name__ == '__main__':
    main()