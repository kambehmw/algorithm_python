def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1

    elems = set()
    min_val, max_val = float('inf'), float('-inf')
    for a in A:
        min_val = min(min_val, a)
        max_val = max(max_val, a)
        elems.add(a)

    for i in range(min_val, max_val+1):
        if i not in elems:
            return i

if __name__ == '__main__':
    A = [2, 3, 1, 5]
    print(solution(A))