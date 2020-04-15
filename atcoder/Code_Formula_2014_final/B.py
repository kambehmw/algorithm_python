n = int(input())
ans = 0
ans += 3 * (n // 2)
ans -= 2 * (n // 2)
ans += 3 * (n % 2)
print(ans)