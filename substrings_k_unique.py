# substrings_k_unique.py
def uniqueSubstring(s, k):
    res = set()
    i = 0
    while i <= len(s) - k:
        temp = s[i : i + k]
        if len(set(temp)) == len(temp):
            res.add(str(temp))
        i += 1
    return list(res)


s = "awaglknagawunagwkwagl"
k = 4
res = uniqueSubstring(s, k)
print(res)
# 23280666519454
