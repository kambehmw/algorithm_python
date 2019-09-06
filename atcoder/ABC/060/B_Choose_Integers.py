A, B ,C = list(map(int, input().split()))
for i in range(A, B*A+1, A):
    if i % B == C:
        print("YES")
        exit()
print("NO")