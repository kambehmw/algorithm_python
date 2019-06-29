def main():
    S = input()
    str_dict = {}
    for s in S:
        if s not in str_dict:
            str_dict[s] = 0
        str_dict[s] += 1

    if len(str_dict) == 2:
        for value in str_dict.values():
            if value != 2:
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()