# SortClassObjects.py
from operator import attrgetter


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return "User {}:{}".format(self.user_id, self.name)


users = [
    User(7, "Ali"),
    User(9, "Canlin"),
    User(29, "Alanna"),
    User(54, "Tim"),
    User(17, "Salman"),
    User(91, "Katie"),
    User(71, "Alia"),
    User(10, "Daniel"),
]
print(sorted(users, key=lambda u: u.user_id))
print(sorted(users, key=attrgetter("name")))
