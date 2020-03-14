N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
x = ["" for _ in range(N)]
ans = 0
for i in range(N):
    if K <= i:
        if T[i] == "r":
            if x[i-K] == "p":
                if i + K < N:
                    if T[i+K] == "s":
                        x[i] = "s"
                    else:
                        x[i] = "r"
                else:
                    x[i] = "r"
            else:
                ans += P
                x[i] = "p"
        elif T[i] == "s":
            if x[i-K] == "r":
                if i + K < N:
                    if T[i + K] == "p":
                        x[i] = "p"
                    else:
                        x[i] = "s"
                else:
                    x[i] = "s"
            else:
                ans += R
                x[i] = "r"
        elif T[i] == "p":
            if x[i-K] == "s":
                if i + K < N:
                    if T[i + K] == "r":
                        x[i] = "r"
                    else:
                        x[i] = "p"
                else:
                    x[i] = "p"
            else:
                ans += S
                x[i] = "s"
    else:
        if T[i] == "r":
            ans += P
            x[i] = "p"
        elif T[i] == "s":
            ans += R
            x[i] = "r"
        elif T[i] == "p":
            ans += S
            x[i] = "s"
print(ans)