X = int(input())
if X == 1:
    print(1)
    exit()

ans = 0
for b in range(1, X+1):
    for p in range(2, X+1):
        pow = b ** p
        if pow <= X:
            ans = max(ans, pow)
        else:
            break
print(ans)