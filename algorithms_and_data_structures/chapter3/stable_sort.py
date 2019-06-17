from collections import namedtuple
import copy

Card = namedtuple('Card', ('suit', 'value'))

def bubble(A):
    for i in range(0, len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j].value < A[j-1].value:
                A[j], A[j-1] = A[j-1], A[j]

def selection(A):
    for i in range(0, len(A)):
        minj = i
        for j in range(i, len(A)):
            if A[j].value < A[minj].value:
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]

def print_info(A):
    s = [a[0] + str(a[1]) for a in A]
    print(" ".join(s))

def is_stable(C1, C2):
    for c1, c2 in zip(C1, C2):
        if c1.suit != c2.suit:
            return False
    return True

def main():
    N = int(input())
    C1 = []
    for c in input().split():
        C1.append(Card(suit=c[0], value=int(c[1])))

    C2 = copy.deepcopy(C1)

    bubble(C1)
    selection(C2)

    print(C1)
    print("Stable")
    print(C2)
    if is_stable(C1, C2):
        print("Stable")
    else:
        print("Not stable")

if __name__ == '__main__':
    main()
