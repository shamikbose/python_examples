# MostFrequentCounts.py
list_a = ["a", "b", "c", "f", "a", "e", "f", "c", "g", "g"]
from collections import Counter

counts = Counter(list_a)
top_two = counts.most_common(2)
print(top_two)
