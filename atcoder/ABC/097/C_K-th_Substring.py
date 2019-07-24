def get_char_ngram(n, s):
    char_gram = [''.join(s[i:i+n]) for i in range(len(s)-n+1)]
    return char_gram

s = input()
K = int(input())
res = set()
for i in range(1, K+1):
    tmp = set(get_char_ngram(i, s))
    res = res.union(tmp)
res = sorted(list(res))
print(res[K-1])