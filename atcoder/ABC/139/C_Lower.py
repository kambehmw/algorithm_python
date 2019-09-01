N = int(input())
H = list(map(int, input().split()))
if N == 1:
    print(0)
    exit()
reverse_H = H[::-1]
ans = 0
result = []
for i in range(N-1):
    if reverse_H[i] <= reverse_H[i+1]:
        ans += 1
    else:
        result.append(ans)
        ans = 0
if ans > 0:
    result.append(ans)
if result:
    print(max(result))
else:
    print(0)