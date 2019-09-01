N = int(input())
V = list(map(int, input().split()))
odd, even = {}, {}
for i in range(N):
    if i % 2 == 1:
        if V[i] not in even:
            even[V[i]] = 0
        even[V[i]] += 1
    else:
        if V[i] not in odd:
            odd[V[i]] = 0
        odd[V[i]] += 1

sorted_odd = sorted(odd.items(), key=lambda x: x[1], reverse=True)
sorted_even = sorted(even.items(), key=lambda x: x[1], reverse=True)
if sorted_odd[0][0] != sorted_even[0][0]:
    print(N - sorted_even[0][1] - sorted_odd[0][1])
else:
    if len(sorted_odd) == 1 or len(sorted_even) == 1:
        print(N // 2)
    else:
        print(N - max(sorted_even[0][1] + sorted_odd[1][1], sorted_even[1][1] + sorted_odd[0][1]))