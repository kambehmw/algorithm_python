N, A, B = map(int, input().split())
cnt = 0
cnt += N // (A + B) * A
mod = N % (A + B)
if mod <= A:
    cnt += mod
else:
    cnt += A
print(cnt)