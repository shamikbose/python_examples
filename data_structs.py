def add(x, y):
    return x + y


def cube(x):
    return x * x * x


res = [(a, b) for a in range(1, 100) for b in range(1, 1000) if (b == a * a)]
print res
print map(cube, range(3, 6))
print reduce(add, range(1, 10))
# sets
list1 = [1, 3, 1, 7, 9, 12, 1, 54, 0, 87]
set_from_list = set(list1)
print set_from_list
# dictionaries
dir1 = {"a": 123, "b": 124, "c": 125}
print dir1.keys()
