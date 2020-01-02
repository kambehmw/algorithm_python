from collections import defaultdict

def solution(A):
    if len(A) == 0:
        return -1

    val2indices = defaultdict(list)
    for i, a in enumerate(A):
        val2indices[a].append(i)

    half = len(A) // 2
    max_len = 0
    indices = None
    for k, v in val2indices.items():
        if max_len < len(v):
            max_len = len(v)
            indices = v
    if half < len(indices):
        return indices[0]
    else:
        return -1


if __name__ == '__main__':
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    print(solution(A))