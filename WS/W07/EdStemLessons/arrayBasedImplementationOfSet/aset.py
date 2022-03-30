"""
    Array-based implementation of Set ADT.
"""

from __future__ import annotations
from set import *
from referential_array import ArrayR


class ASet(Set[T]):
    """Simple array-based implementation of the set ADT.

    Attributes:
         size (int): number of elements in the set
         array (ArrayR[T]): array storing the elements of the set

    ArrayR cannot create empty arrays. So default capacity value 1
    is used to avoid this.
    """

    MIN_CAPACITY = 1

    def __init__(self, capacity: int = 1) -> None:
        """ Initialization. """
        Set.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, capacity))

    def __len__(self) -> int:
        """ Returns the number of elements in the set. """
        return self.size

    def is_empty(self) -> bool:
        """ True if the set is empty. """
        return len(self) == 0  # len(self) same as self.__len__()

    def __contains__(self, item: T) -> bool:
        """ True if the set contains the item. """
        for i in range(self.size):
            if item == self.array[i]:
                return True
        return False

    def clear(self) -> None:
        """ Makes the set empty. """
        self.size = 0

    def is_full(self) -> bool:
        """ True if the set is full and no element can be added. """
        return len(self) == len(self.array)

    def add(self, item: T) -> None:
        """ Adds an element to the set. Note that an element already
        present in the set should not be added.
        :pre: the set is not full
        :raises Exception: if the set is full.
        """
        if self.is_full():
            raise Exception("Set is full")
        if item not in self:  # same as if self.__contains__(item):
            self.array[self.size] = item
            self.size += 1

    def remove(self, item: T) -> None:
        """ Removes an element from the set.
        :pre: the element should be present in the set
        :raises KeyError: if no such element is found.
        """
        if item not in self:
            raise KeyError("Item not in set")
        for i in range(self.size):
            if item == self.array[i]:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                break

    def union(self, other: ASet[T]) -> ASet[T]:
        """ Creates a new set equal to the union with another one,
        i.e. the result set should contains the elements of self and other.
        """
        maxcapacity = len(self.array) + len(other.array)
        res = ASet(maxcapacity)
        for the_set in [self, other]:
            for i in range(len(the_set)):
                res.add(the_set.array[i])
        return res

    def intersection(self, other: ASet[T]) -> ASet[T]:
        """ Creates a new set equal to the intersection with another one,
        i.e. the result set should contain the elements that are both in 
        self *and* other.
        """
        res = ASet(min(len(self), len(other)))
        for i in range(len(self)):
            if self.array[i] in other:
                res.add(self.array[i])
        return res

    def difference(self, other: ASet[T]) -> ASet[T]:
        """ Creates a new set equal to the difference with another one,
        i.e. the result set should contain the elements of self that 
        *are not* in other.
        """
        result = ASet(self.size)
        for i in range(len(self)):
            if self.array[i] not in other:
                result.add(self.array[i])
        return result