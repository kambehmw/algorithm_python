def minimize(H, W):
    ans = float('inf')
    for h in range(1, H):
        sa = h * W
        sb = (H - h) * (W // 2)
        sc = (H - h) * (W - W // 2)
        smax = max(sa, sb, sc)
        smin = min(sa, sb, sc)
        ans = min(ans, smax - smin)

        sb = W * ((H - h) // 2)
        sc = W * (H - h - (H - h) // 2)
        smax = max(sa, sb, sc)
        smin = min(sa, sb, sc)
        ans = min(ans, smax - smin)
    return ans

H, W = tuple(map(int, input().split()))
ans1 = minimize(H, W)
ans2 = minimize(W, H)
print(min(ans1, ans2))