S = input()
counters = {c: 0 for c in ["A", "B", "C", "D", "E", "F"]}
for c in S:
    counters[c] += 1
print(" ".join([str(v) for k, v in sorted(counters.items())]))