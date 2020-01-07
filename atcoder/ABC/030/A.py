A, B, C, D = tuple(map(int, input().split()))
if B / A < D / C:
    print("AOKI")
elif B / A > D / C:
    print("TAKAHASHI")
else:
    print("DRAW")
