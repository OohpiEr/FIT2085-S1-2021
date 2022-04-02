""" Linked-node based implementation of List ADT. """
from node import Node
from abstract_list import List, T

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'


class LinkedList(List[T]):
    """ List ADT implemented with linked nodes. """

    def __init__(self, dummy_capacity=1) -> None:
        """ Linked-list object initialiser. """
        List.__init__(self)  # Could use super(LinkedList, self).__init__() instead
        self.head = None

    def clear(self):
        """ Clear the list. """
        # first call clear() for the base class
        List.clear(self)
        self.head = None

    def __setitem__(self, index: int, item: T) -> None:
        """ Magic method. Insert the item at a given position. """
        current = self.__get_node_at_index(index)
        current.item = item

    def __getitem__(self, index: int) -> T:
        """ Magic method. Return the element at a given position. """
        current = self.__get_node_at_index(index)
        return current.item

    def index(self, item: T) -> int:
        """ Find the position of a given item in the list. """
        current = self.head
        index = 0
        while current is not None and current.item != item:
            current = current.next
            index += 1
        if current is None:
            raise ValueError('Item is not in list')
        else:
            return index

    def __get_node_at_index(self, index: int) -> Node[T]:
        """ Get node object at a given position. """
        if 0 <= index and index < len(self):
            current = self.head
            for i in range(index):
                current = current.next
            return current
        else:
            raise ValueError('Index out of bounds')

    def delete_at_index(self, index: int) -> T:
        """ Delete item at a given position. """
        try:
            prev_node = self.__get_node_at_index(index - 1)
        except ValueError as e:
            if index == 0:
                item = self.head.item
                self.head = self.head.next
            elif self.is_empty():
                raise ValueError('list is empty')
            else:
                raise e
        else:
            item = prev_node.next.item
            prev_node.next = prev_node.next.next
        self.length -= 1
        return item

    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        newnode = Node(item)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
        else:
            prev_node = self.__get_node_at_index(index - 1)
            newnode.next = prev_node.next
            prev_node.next = newnode
        self.length += 1
