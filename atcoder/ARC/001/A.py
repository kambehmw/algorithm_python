N = int(input())
c = input()
d = {"1": 0, "2": 0, "3": 0, "4": 0}
for x in c:
    d[x] += 1
print(max(d.values()), min(d.values()))