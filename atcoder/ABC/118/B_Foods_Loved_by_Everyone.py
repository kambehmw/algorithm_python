N, M = map(int, input().split())
ans = {i for i in range(1, M+1)}
for i in range(N):
    tmp = list(map(int, input().split()))
    K, A = tmp[0], tmp[1:]
    ans = ans.intersection(set(A))
print(len(ans))
