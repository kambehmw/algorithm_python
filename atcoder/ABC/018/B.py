S = input()
N = int(input())
L, R = [], []
for _ in range(N):
    l, r = tuple(map(int, input().split()))
    L.append(l)
    R.append(r)

for l, r in zip(L, R):
    l -= 1
    S = S[:l] + S[l:r][::-1] + S[r:]
print(S)