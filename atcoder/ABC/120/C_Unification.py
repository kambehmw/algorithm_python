S = input()
char_count = {"0": 0, "1": 0}
for s in S:
    char_count[s] += 1
print(2 * min(char_count.values()))