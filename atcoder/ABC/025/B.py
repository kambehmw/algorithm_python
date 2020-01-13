N, A, B = tuple(map(int, input().split()))
S, D = [], []
for _ in range(N):
    s, d = input().split()
    S.append(s)
    D.append(int(d))

pos = 0
for s, d in zip(S, D):
    if d < A:
        move = A
    elif B < d:
        move = B
    else:
        move = d

    if s == "East":
        pos += move
    else:
        pos -= move

if pos > 0:
    print("East {}".format(pos))
elif pos < 0:
    print("West {}".format(abs(pos)))
else:
    print(0)