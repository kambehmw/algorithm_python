import time

def is_feasible_travel(N, t, x, y):
    t_old, x_old, y_old = t[0], x[0], y[0]
    if N == 1:
        if t_old < (x_old + y_old):
            return False
        if (t_old % 2) == ((x_old + y_old) % 2):
            return True
        else:
            return False

    for ti, xi, yi in zip(t[1:], x[1:], y[1:]):
        t_diff = ti - t_old
        x_diff = abs(xi - x_old)
        y_diff = abs(yi - y_old)

        dist = x_diff + y_diff
        if dist > t_diff:
            return False
        elif dist < t_diff:
            if (dist % 2) != (t_diff % 2):
                return False

        t_old, x_old, y_old = ti, xi, yi
    return True


def main():
    N = int(input())
    t = [0] * N
    x = [0] * N
    y = [0] * N
    for i in range(N):
        t[i], x[i], y[i] = map(int, input().split())

    # start = time.time()
    if is_feasible_travel(N, t, x, y):
        print("Yes")
    else:
        print("No")
    # print(time.time() - start)


if __name__ == '__main__':
    main()
