N = int(input())
if N == 1:
    print(1)
    exit()
max_count = 0
ans = 0
for i in range(1, N+1):
    tmp_i = i
    count = 0
    while True:
        if tmp_i % 2 == 0:
            count += 1
            tmp_i = tmp_i // 2
        else:
            if max_count < count:
                ans = i
                max_count = count
            break
print(ans)