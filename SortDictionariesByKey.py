# SortDictionariesByKey.py
rows = [
    {"fname": "Brian", "lname": "Jones", "uid": 1003},
    {"fname": "David", "lname": "Beazley", "uid": 1002},
    {"fname": "John", "lname": "Cleese", "uid": 1001},
    {"fname": "Big", "lname": "Jones", "uid": 1004},
    {"fname": "Chase", "lname": "Jones", "uid": 1005},
]
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))
rows_by_lfname = sorted(rows, key=itemgetter("lname", "fname"))
print("Sorted by first name")
print(rows_by_fname)
print("Sorted by ID")
print(rows_by_uid)
print("Sorted by last/first name")
print(rows_by_lfname)
