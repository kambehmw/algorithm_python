H, W = map(int, input().split())
cnt = H * (W - 1) if W - 1 > 0 else 0
cnt += W * (H - 1) if H - 1 > 0 else 0
print(cnt)