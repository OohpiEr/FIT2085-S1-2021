""" Kist ADT and an array implementation.

Defines a generic abstract list with the usual methods, and implements
a list using arrays.
"""
__author__ = "Maria Garcia de la Banda for the base" + "XXXXX student for"
__docformat__ = 'reStructuredText'

import math
import unittest
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from referential_array import ArrayR, T


class List(ABC, Generic[T]):
    """ Abstract class for a generic List. """

    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        pass

    @abstractmethod
    def append(self, item: T) -> None:
        pass

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        pass

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        pass

    def remove(self, item: T) -> None:
        index = self.index(item)
        self.delete_at_index(index)

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self):
        self.length = 0


class ArrayList(List[T]):
    MIN_CAPACITY = 1

    def __init__(self, max_capacity: int) -> None:
        List.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def __getitem__(self, index: int) -> T:
        return self.array[index]

    def __setitem__(self, index: int, value: T) -> None:
        self.array[index] = value

    def index(self, item: T) -> int:
        for i in range(len(self)):
            if item == self.array[i]:
                return i
        raise ValueError("item not in list")

    def delete_at_index(self, index: int) -> T:
        """ deletes the element at index and returns the element.
        :pre: position of index must be in the list
        :raises Exception: if position of index is not in the list (done by python)
        """
        item = self.array[index]
        self.length -= 1
        for i in range(index, self.length):
            self.array[i] = self.array[i + 1]

    def __newsize(self) -> int:
        """ Returns the new capacity, according to whatever formula you want to define. """
        return math.ceil(len(self) * 1.125)

    def insert(self, index: int, item: T) -> None:
        """ Adds an element at the index of the list. """
        if len(self) == len(self.array):
            new_array = ArrayR(self.__newsize())
            for i in range(len(self)):
                new_array[i] = self.array[i]
            self.array = new_array
        self.array[index] = item
        self.length += 1

    # def append(self, item: T) -> None:
    #     """ Adds an element to the rear of the list. """
    #     if len(self) == len(self.array):
    #         new_array = ArrayR(self.__newsize())
    #         for i in range(len(self)):
    #             new_array[i] = self.array[i]
    #         self.array = new_array
    #     self.array[len(self)] = item
    #     self.length += 1

    def append(self, item: T) -> None:
        """ Adds an element to the rear of the list. """
        self.insert(len(self), item)
