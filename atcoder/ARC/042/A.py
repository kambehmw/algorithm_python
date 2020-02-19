N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
A = A[::-1]
s = [False] * N
ans = []
for a in A:
    if s[a-1]:
        continue
    ans.append(a)
    s[a-1] = True
for i, x in enumerate(s, 1):
    if not x:
        ans.append(i)
print("\n".join(map(str, ans)))