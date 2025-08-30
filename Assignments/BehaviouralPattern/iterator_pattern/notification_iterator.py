# ---------- Concrete Iterator ----------
from iterator import Iterator

class NotificationIterator(Iterator):
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._items):
            item = self._items[self._index]
            self._index += 1
            return item
        raise StopIteration
    
"""
Module Type → Concrete implementation of Iterator.

Purpose →

Knows how to traverse the collection (self._index).

Implements Python’s iterator protocol (__iter__, __next__).

Significance → Separates traversal logic from collection logic.
The collection just stores notifications; the iterator knows how to step through them one by one.
"""