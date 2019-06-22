def main():
    N = int(input())
    AB = []
    for _ in range(N):
        temp = list(map(int, input().split()))
        AB.append((temp[0], temp[1]))

    sorted_AB = sorted(AB, key=lambda x: x[1])

    total_time = 0
    flag = True
    for x in sorted_AB:
        total_time += x[0]
        if total_time > x[1]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()