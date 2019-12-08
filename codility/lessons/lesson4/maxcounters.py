def solution(N, A):
    # write your code in Python 3.6
    counter = {i: 0 for i in range(1, N+1)}
    max_val = 0
    last_max = 0
    for a in A:
        if a == N+1:
            last_max = max_val
        else:
            if counter[a] < last_max:
                counter[a] = last_max + 1
            else:
                counter[a] += 1

            if max_val < counter[a]:
                max_val = counter[a]

    for k, v in counter.items():
        if v < last_max:
            counter[k] = last_max

    return list(counter.values())

if __name__ == '__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))