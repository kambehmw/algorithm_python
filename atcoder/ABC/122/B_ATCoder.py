def main():
    S = input()

    acgt = []
    flag = False
    count = 0
    for s in S:
        if s == "A" or s == "C" or s == "G" or s == "T":
            if flag:
                count += 1
            else:
                flag = True
                count = 1
        else:
            acgt.append(count)
            flag = False
            count = 0

    if count > 0:
        acgt.append(count)

    print(max(acgt))


if __name__ == '__main__':
    main()