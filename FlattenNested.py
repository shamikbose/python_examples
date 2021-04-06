# FlattenNested.py
from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


items = [4, 9, [3, 1, 5, [9, 2], 5], 17, 31]
for x in flatten(items):
    print(x)
