W = input()
vowels = {'a', 'i', 'u', 'e', 'o'}
ans = ""
for w in W:
    if w not in vowels:
        ans += w
print(ans)