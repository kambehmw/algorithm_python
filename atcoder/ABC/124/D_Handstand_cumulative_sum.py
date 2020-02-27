N, K = map(int, input().split())
S = input()
nums = []
now = 1
cnt = 0
for i in range(N):
    if S[i] == str(now):
        cnt += 1
    else:
        nums.append(cnt)
        now = 1 - now
        cnt = 1
if cnt != 0:
    nums.append(cnt)
if len(nums) % 2 == 0:
    nums.append(0)

csum = [0] * (len(nums) + 1)
for i in range(len(nums)):
    csum[i + 1] = csum[i] + nums[i]

add = 2 * K + 1
ans = 0
tmp = 0
for i in range(0, len(nums), 2):
    left = i
    right = min(i + add, len(nums))
    tmp = csum[right] - csum[left]
    ans = max(ans, tmp)
print(ans)