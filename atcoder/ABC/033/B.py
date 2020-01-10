N = int(input())
S, P = [], []
for _ in range(N):
    s, p = input().split()
    S.append(s)
    P.append(int(p))
total = sum(P)
max_val = max(P)
max_idx = P.index(max_val)
if total // 2 < max_val:
    print(S[max_idx])
else:
    print("atcoder")
