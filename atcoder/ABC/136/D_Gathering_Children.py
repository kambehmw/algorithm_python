S = input()
N = len(S)
r_cnt = 1
l_cnt = 0
idx = 0
ans = [0] * N
for i in range(1, N):
    if S[i-1] == "L" and S[i] == "R":
        if (r_cnt + l_cnt) % 2 == 0:
            ans[idx-1] = (r_cnt + l_cnt) // 2
            ans[idx] = (r_cnt + l_cnt) // 2
        else:
            if l_cnt % 2 == 0:
                ans[idx-1] = (r_cnt + l_cnt) // 2 + 1
                ans[idx] = (r_cnt + l_cnt) // 2
            else:
                ans[idx - 1] = (r_cnt + l_cnt) // 2
                ans[idx] = (r_cnt + l_cnt) // 2 + 1
        r_cnt = 0
        l_cnt = 0

    elif S[i-1] == "R" and S[i] == "L":
        idx = i
    if S[i] == "R":
        r_cnt += 1
    elif S[i] == "L":
        l_cnt += 1

if (r_cnt + l_cnt) % 2 == 0:
    ans[idx - 1] = (r_cnt + l_cnt) // 2
    ans[idx] = (r_cnt + l_cnt) // 2
else:
    if l_cnt % 2 == 0:
        ans[idx - 1] = (r_cnt + l_cnt) // 2 + 1
        ans[idx] = (r_cnt + l_cnt) // 2
    else:
        ans[idx - 1] = (r_cnt + l_cnt) // 2
        ans[idx] = (r_cnt + l_cnt) // 2 + 1
print(*ans)