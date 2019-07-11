def check_double_block(start, end, S):
    for i in range(start, end):
        if S[i] == "#" and S[i+1] == "#":
            return False
    return True

def main():
    N, A, B, C, D = list(map(int, input().split()))
    S = input()

    S = "#" + S + "#"

    if C < D:
        if not check_double_block(A, C, S) or not check_double_block(B, D, S):
            print("No")
        else:
            print("Yes")
    else:
        for i in range(B, D+1):
            if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
                print("Yes")
                exit()
        print("No")


if __name__ == '__main__':
    main()