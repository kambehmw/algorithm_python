N = int(input())
T = list(map(int, input().split()))
M = int(input())
P, X = [], []
for i in range(M):
    p, x = map(int, input().split())
    P.append(p)
    X.append(x)

total_time = sum(T)
for i in range(M):
    index = P[i] - 1
    tmp_diff = X[i] - T[index]
    print(total_time + tmp_diff)