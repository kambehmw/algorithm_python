N = int(input())
ans = ""
while True:
    ans = str(abs(N % -2)) + ans
    N += N % -2
    N = N // -2
    if N == 0:
        break
print(ans)