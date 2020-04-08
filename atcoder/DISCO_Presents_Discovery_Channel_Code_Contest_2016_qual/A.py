s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
W = int(input())
N = len(s)
for i in range(0, N, W):
    print(s[i:i+W])