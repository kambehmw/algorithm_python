A, B, K = list(map(int, input().split()))
ans = set()
for i in range(K):
    if A <= A+i <= B:
        ans.add(A+i)
    if A <= B-i <= B:
        ans.add(B-i)
for x in sorted(ans):
    print(x)