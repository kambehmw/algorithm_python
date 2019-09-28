s = input()
K = int(input())
base_count = ord("z") + 1
ans = ""
for c in s:
    t = (base_count - ord(c)) % 26
    if t <= K:
        ans += "a"
        K -= t
    else:
        ans += c
if K > 0:
    K = K % 26
    ans = ans[:-1] + chr((ord(ans[-1]) + K))
print(ans)