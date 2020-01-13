s = input()
k = int(input())
ans = set()
for i in range(len(s)-k+1):
    if len(s[i:i+k]) == k:
        ans.add(s[i:i+k])
print(len(ans))