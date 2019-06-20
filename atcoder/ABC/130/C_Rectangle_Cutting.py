def main():
    W, H, x, y = list(map(int, input().split()))
    split_num = int((x + x) == W and (y + y) == H)
    print("{:.6f} {}".format((W * H) / 2.0, split_num))

if __name__ == '__main__':
    main()