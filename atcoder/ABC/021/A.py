N = int(input())
bin_str = bin(N)[2:]
count = sum([1 if c == "1" else 0 for c in bin_str])
print(count)
for i, c in enumerate(bin_str[::-1]):
    if c != "0":
        print(int(c) * 2 ** i)
