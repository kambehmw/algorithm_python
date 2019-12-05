import math

def solution(X, Y, D):
    # write your code in Python 3.6
    return math.ceil((Y - X) / D)

if __name__ == '__main__':
    X = 10
    Y = 85
    D = 30
    print(solution(X, Y, D))