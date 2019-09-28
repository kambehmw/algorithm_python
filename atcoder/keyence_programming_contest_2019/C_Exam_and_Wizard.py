N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ok = []
S = 0
ans = 0
for a, b in zip(A, B):
    if a >= b:
        ok.append(a - b)
    else:
        ans += 1
        S += (b - a)
ok.sort()
while S > 0 and ok:
    ans += 1
    S -= ok.pop()

ans = -1 if S > 0 else ans
print(ans)