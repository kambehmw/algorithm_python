N = int(input())
S, T = [], []
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))
X = input()
ans = sum(T)
partial_sum = 0
for s, t in zip(S, T):
    partial_sum += t
    if s == X:
        break
print(ans - partial_sum)
