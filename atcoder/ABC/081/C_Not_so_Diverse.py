def main():
    N, K = input().split()
    A = list(map(int, input().split()))

    id2count = {}
    for x in A:
        if x not in id2count:
            id2count[x] = 1
        else:
            id2count[x] += 1

    sorted_items = sorted(id2count.items(), key=lambda x: x[1])
    total = 0
    for (key, count) in sorted_items[:len(sorted_items)-int(K)]:
        total += count
    print(total)


if __name__ == '__main__':
    main()