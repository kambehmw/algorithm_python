A, B, C, K = tuple(map(int, input().split()))
S, T = tuple(map(int, input().split()))
if S + T < K:
    print(S * A + T * B)
else:
    print(S * A + T * B - (S + T) * C)
