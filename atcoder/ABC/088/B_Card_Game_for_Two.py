import copy

def main():
    N = int(input())
    A = list(map(int, input().split()))

    p1_total = 0
    p2_total = 0
    for i in range(N):
        if i % 2 == 0:
            tmp = max(A)
            p1_total += tmp
            del A[A.index(tmp)]
        else:
            tmp = max(A)
            p2_total += tmp
            del A[A.index(tmp)]

    print(p1_total - p2_total)

if __name__ == '__main__':
    main()