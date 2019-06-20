def main():
    N = input()
    W = list(map(int, input().split()))
    diff_abs = float('inf')
    for i in range(1, len(W)):
        temp_diff_abs = abs(sum(W[:i]) - sum(W[i:]))
        if temp_diff_abs < diff_abs:
            diff_abs = temp_diff_abs
    print(diff_abs)


if __name__ == '__main__':
    main()
