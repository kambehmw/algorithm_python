def main():
    inputs = input()
    score = sum([1 for s in inputs if s == "1"])
    print(score)


if __name__ == '__main__':
    main()