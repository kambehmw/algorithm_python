n = int(input())
A = list(map(int, input().split()))
max_val = max(A)
half = max_val // 2
r = None
diff = float('inf')
for a in A:
    d = abs(half - a)
    if d < diff and a != max_val:
        diff = d
        r = a
print(max_val, r)