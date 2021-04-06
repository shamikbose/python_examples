# zipFunction.py - This program demonstrates uses of the zip function
import random
from itertools import zip_longest

xpts = [random.randint(0, 10) for x in range(10)]
ypts = [random.randint(0, 100) for x in range(12)]
print(xpts, ypts, sep=",")
for x, y in zip(
    xpts, ypts
):  # zip completes after the SHORTEST seqeunce is extinguished
    print(x, y, sep=":", end=",")
    print(x, y, sep=":", end=",")
print()
for x, y in zip_longest(
    xpts, ypts
):  # zip_longest completes after the LONGEST seqeunce is extinguished
    print(x, y, sep=":", end=",")
