from collections import deque
s = input()
t = input()
d = deque(s)
N = len(s)
cnt = 0
for i in range(N):
    # print(d)
    if "".join(d) == t:
        print(cnt)
        exit()
    d.appendleft(d[-1])
    d.pop()
    cnt += 1
print(-1)