def main():
    N = int(input())
    SP = []
    for _ in range(N):
        temp = input().split()
        SP.append((temp[0], int(temp[1])))

    sorted_SP = sorted(SP, key=lambda x: x[1], reverse=True)
    sorted_SP = sorted(sorted_SP, key=lambda x: x[0])

    indices = [SP.index(x)+1 for x in sorted_SP]
    # print(sorted_SP)
    for i in indices:
        print(i)

if __name__ == '__main__':
    main()