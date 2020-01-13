X = input()
N = len(X)
if N == 0:
    print("YES")
    exit()

i = 0
while i < N:
    if X[i] == "c":
        if not (i + 1 < N and X[i+1] == "h"):
            print("NO")
            exit()
        else:
            i += 2
    elif X[i] == "o" or X[i] == "k" or X[i] == "u":
        i += 1
    else:
        print("NO")
        exit()
print("YES")
