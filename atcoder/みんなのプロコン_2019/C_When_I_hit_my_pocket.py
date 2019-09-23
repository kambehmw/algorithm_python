K, A, B = list(map(int, input().split()))
if (B - A) <= 2:
    print(K+1)
else:
    if (K - 1) < A:
        print(K+1)
    else:
        count = max(0, ((K - (A - 1)) // 2))
        print(A + count * (B - A) + (K - (A - 1)) % 2)
