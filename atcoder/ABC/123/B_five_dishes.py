def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    min_mod = 10
    elapsed_time = 0
    for x in [A, B, C, D, E]:
        mod = x % 10
        if 0 < mod < min_mod:
            min_mod = mod
        time = x if x % 10 == 0 else (x // 10 + 1) * 10
        elapsed_time += time

    elapsed_time = elapsed_time - (10 - min_mod)
    print(elapsed_time)

if __name__ == '__main__':
    main()