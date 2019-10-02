def xor(n):
    ans = None
    if (n + 1) % 2 == 0:
        if ((n + 1) // 2) % 2 == 0:
            ans = 0
        else:
            ans = 1
    else:
        if ((n +  1) // 2) % 2 == 0:
            ans = 0 ^ n
        else:
            ans = 1 ^ n
    return ans

A, B = tuple(map(int, input().split()))
print(xor(A-1) ^ xor(B))