L, X, Y, S, D = map(int, input().split())
if Y <= X:
    if S <= D:
        print((D - S) / (X + Y))
    else:
        print((L - (S - D)) / (X + Y))
else:
    if S <= D:
        print(min((D - S) / (X + Y), (L - (D - S)) / (Y - X)))
    else:
        print(min((L - (S - D)) / (X + Y), (S - D) / (Y - X)))
