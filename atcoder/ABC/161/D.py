import sys
sys.setrecursionlimit(10 ** 6)
ans = []

def dfs(i):
    if 10 < len(i):
        return

    ans.append(int(i))
    if 0 < int(i[-1]):
        dfs(i + chr(ord(i[-1]) - 1))
    if int(i[-1]) < 9:
        dfs(i + chr(ord(i[-1]) + 1))
    dfs(i + i[-1])


K = int(input())
for i in range(1, 10):
    dfs(str(i))
ans.sort()
#print(ans.sort())
# print(ans)
print(ans[K-1])