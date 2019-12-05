from collections import defaultdict

def solution(A):
    # write your code in Python 3.6
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    for k, v in d.items():
        if v % 2 != 0:
            return k


if __name__ == '__main__':
    A = [9, 3, 9, 3, 9, 7, 9]
    print(solution(A))