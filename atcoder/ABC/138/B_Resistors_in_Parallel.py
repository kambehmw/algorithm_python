N = int(input())
A = list(map(int, input().split()))
sum_A = sum([1 / a for a in A])
print(1 / sum_A)