from collections import deque
N, K = map(int, input().split())
V = list(map(int, input().split()))
R = min(N, K)
ans = 0
for A in range(R+1):
    for B in range(R+1):
        d = deque(V)
        if A + B > R:
            continue
        x = []
        for _ in range(A):
            if 0 < len(d):
                x.append(d.popleft())
        for _ in range(B):
            if 0 < len(d):
                x.append(d.pop())
        x.sort()
        drop = K - (A + B)
        for _ in range(drop):
            if 0 < len(x) and x[0] < 0:
                x.pop(0)
        ans = max(ans, sum(x))
print(ans)