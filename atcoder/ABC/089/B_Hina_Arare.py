def main():
    N = int(input())
    S = input().split()

    kind_set = set()
    for s in S:
        kind_set.add(s)

    length = len(kind_set)
    if length == 3:
        print("Three")
    elif length == 4:
        print("Four")

if __name__ == '__main__':
    main()