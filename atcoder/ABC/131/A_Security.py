def main():
    S = input()

    for s1, s2 in zip(S[:-1], S[1:]):
        if s1 == s2:
            print("Bad")
            exit()
    print("Good")


if __name__ == '__main__':
    main()