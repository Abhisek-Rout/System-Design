# ---------- Aggregate Interface ----------

from abc import ABC, abstractmethod

from iterator import Iterator

class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self) -> Iterator:
        pass

"""
Module Type → Abstract Base Class.

Purpose → Provides a factory method create_iterator() for collections.

Any notification collection (like EmailNotifications) must be able to produce an iterator object.

Significance → Enforces that all collections support iteration, but doesn’t dictate how.
"""