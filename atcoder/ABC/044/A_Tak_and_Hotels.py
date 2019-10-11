N = int(input())
K = int(input())
X = int(input())
Y = int(input())
first_half = K * X if N - K > 0 else N * X
rest = N - K if N - K > 0 else 0
print(first_half + rest * Y)