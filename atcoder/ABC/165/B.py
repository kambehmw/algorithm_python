X = int(input())
ans = 100
i = 0
while ans < X:
    ans *= 1.01
    ans = int(ans)
    i += 1
print(i)