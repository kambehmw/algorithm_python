import itertools

def main():
    inputs = list(map(int, input().split()))
    print(sum(min(list(itertools.permutations(inputs, 2)))))

if __name__ == '__main__':
    main()