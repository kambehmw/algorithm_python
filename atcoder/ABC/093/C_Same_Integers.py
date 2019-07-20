A, B, C = map(int, input().split())
max_num = max(A, B, C)
count = A + B + C
ans = 0
while True:
    if count % 3 == 0 and count / 3 >= max_num:
        break
    else:
        count += 2
        ans += 1
print(ans)
