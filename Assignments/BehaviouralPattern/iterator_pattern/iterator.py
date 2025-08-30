from abc import ABC, abstractmethod

# ---------- Iterator Interfaces ----------
class Iterator(ABC):
    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __next__(self):
        pass

"""
Note:
Module Type → Abstract Base Class (ABC).

Purpose → Defines the contract for all iterators in the system.

Any custom iterator (like NotificationIterator) must provide:

__iter__ → makes the object iterable in for loops.

__next__ → defines how to fetch the next element.

Significance → Decouples the iteration mechanism from the actual data structure (list, set, dict, etc.).
"""