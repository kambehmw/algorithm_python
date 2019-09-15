X = int(input())
ans = 0
i = 1
count = 0
while True:
    count += 1
    ans += i
    if X <= ans:
        break
    i += 1
print(count)