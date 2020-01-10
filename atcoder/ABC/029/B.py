S = [input() for _ in range(12)]
cnt = 0
for s in S:
    chars = set(s)
    if 'r' in chars:
       cnt += 1
print(cnt)
