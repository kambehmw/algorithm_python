A, B = map(int, input().split())
if B == 1:
    print(0)
    exit()
ans = 1
count = A
while True:
    if count >= B:
        break
    ans += 1
    count += (A - 1)
print(ans)