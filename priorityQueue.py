import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        # This is maintained so that items with the same priority can be ordered properly
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


q = PriorityQueue()
q.push(Item("a"), 1)
q.push(Item("b"), 1)
q.push(Item("c"), 7)
q.push(Item("d"), 3)
q.push(Item("e"), 5)
q.push(Item("f"), 1)
for _ in range(6):
    print(q.pop())
