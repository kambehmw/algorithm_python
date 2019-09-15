N = int(input())
A = [int(input()) for _ in range(N)]
num_set = set()
for a in A:
    if a not in num_set:
        num_set.add(a)
    else:
        num_set.remove(a)
print(len(num_set))