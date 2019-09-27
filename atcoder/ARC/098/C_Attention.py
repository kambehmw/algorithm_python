N = int(input())
S = input()
count_e = [0] * N
count_w = [0] * N
for i in range(N-1):
    if S[i] == "W":
        count_w[i+1] = count_w[i] + 1
    else:
        count_w[i+1] = count_w[i]

    if S[N-i-1] == "E":
        count_e[i+1] = count_e[i] + 1
    else:
        count_e[i+1] = count_e[i]

count_e = count_e[::-1]
ans = float('inf')
for i in range(N):
    ans = min(ans, count_w[i] + count_e[i])
print(ans)