from collections import deque
Q, L = map(int, input().split())
d1 = deque()
d2 = deque()
for _ in range(Q):
    q = input().split()
    if q[0] == "Push":
        n, m = int(q[1]), int(q[2])
        if L - n < sum(d2):
            print("FULL")
            exit()
        d1.append(m)
        d2.append(n)
    elif q[0] == "Pop":
        n = int(q[1])
        if sum(d2) < n:
            print("EMPTY")
            exit()
        while 0 < n:
            p = d2.pop()
            if p <= n:
                n -= p
                d1.pop()
            else:
                p -= n
                n = 0
                d2.append(p)
    elif q[0] == "Top":
        if len(d1) == 0:
            print("EMPTY")
            exit()
        p = d1.pop()
        print(p)
        d1.append(p)
    elif q[0] == "Size":
        print(sum(d2))
print("SAFE")
