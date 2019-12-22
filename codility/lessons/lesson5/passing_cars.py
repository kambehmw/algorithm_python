def solution(A):
    cnt = 0
    cnt_cars_traveling_east = 0
    for a in A:
        if a == 0:
            cnt_cars_traveling_east += 1
        else:
            cnt += cnt_cars_traveling_east
            if cnt > 10**9:
                return -1
    return cnt

if __name__ == '__main__':
    A = [0, 1, 0, 1, 1]
    print(solution(A))