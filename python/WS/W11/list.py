""" List ADT and an array implementation.

Defines a generic abstract list with the usual methods, and implements 
a list using arrays and linked nodes. It also includes a linked list iterator.
Also defines UnitTests for the class.
"""
__author__ = "Maria Garcia de la Banda, modified by Brendon Taylor"
__docformat__ = 'reStructuredText'

import unittest
from abc import ABC, abstractmethod 
from enum import Enum
from typing import Generic, type
from referential_array import ArrayR, T


class List(ABC, Generic[T]):
    """ Abstract class for a generic List. """

    def __init__(self) -> None:
        """ Initialises the length of an exmpty list to be 0. """
        self.length = 0

    @abstractmethod
    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the value of the element at position index to be item
        :pre: index is 0 <= index < len(self)
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index
        :pre: index is 0 <= index < len(self)
        """
        pass

    def __len__(self) -> int:
        """ Returns the length of the list
        :complexity: O(1) 
        """
        return self.length

    @abstractmethod
    def is_full(self) -> bool:
        """ Returns True iff the list is full
        """
        pass

    def is_empty(self) -> bool:
        """ Returns True iff the list is empty
        :complexity: O(1) 
        """
        return len(self) == 0

    def clear(self):
        """ Sets the list back to empty
        :complexity: O(1) 
        """
        self.length = 0

    @abstractmethod
    def insert(self, index: int, item: T) -> None:
        """ Moves self[j] to self[j+1] if j>=index, sets self[index]=item
        :pre: index is 0 <= index <= len(self)
        """
        pass

    def append(self, item: T) -> None:
        """ Adds the item to the end of the list; the rest is unchanged. 
        :see: #insert(index: int, item: T) 
        """
        self.insert(len(self), item)

    @abstractmethod
    def delete_at_index(self, index: int) -> T:
        """Moved self[j+1] to self[j] if j>index & returns old self[index]
        :pre: index is 0 <= index < len(self)
        """
        pass

    @abstractmethod
    def index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item
        :raises ValueError: if item not in the list
        """
        pass

    def remove(self, item: T) -> None:
        """ Removes the first occurrence of the item from the list
        :raises ValueError: if item not in the list
        :see: #index(item: T) and #delete_at_index(index: int)
        """
        index = self.index(item)
        self.delete_at_index(index)

    def __str__(self) -> str:
        """ Converts the list into a string, first to last
        :complexity: O(len(self) * M), M is the size of biggest item
        """
        result = "["
        for i in range(len(self)):
            if i > 0:
                result += ', '
            result += str(self[i])
        result += ']'
        return result


class ArrayList(List[T]):
    """ Implementation of a generic list with arrays.
    
    Attributes:
         length (int): number of elements in the list (inherited)
         array (ArrayR[T]): array storing the elements of the list

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """
    MIN_CAPACITY = 1
    
    def __init__(self, max_capacity: int) -> None:
        """ Initialises self.length by calling its parent and 
        self.array as an ArrayList of appropriate capacity
        :complexity: O(len(self)) always due to the ArrarR call
        """        
        List.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))

    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index
        :pre: index is 0 <= index < len(self) checked by ArrayR's method
        :complexity: O(1)
        """
        return self.array[index]
    
    def __setitem__(self, index: int, value: T) -> None:
        """ Sets the value of the element at position index to be item
        :pre: index is 0 <= index < len(self) checked by ArrayR's method
        :complexity: O(1)
        """
        self.array[index] = value

    def __shuffle_right(self, index: int) -> None:
        """ Shuffles all the items to the right from index
        :complexity best: O(1) shuffle from the end of the list
        :complexity worst: O(N) shuffle from the start of the list
        where N is the number of items in the list
        """
        for i in range(len(self), index, -1):
            self.array[i] = self.array[i - 1]

    def __shuffle_left(self, index: int) -> None:
        """ Shuffles all the items to the left from index
        :complexity best: O(1) shuffle from the start of the list
        :complexity worst: O(N) shuffle from the end of the list
        where N is the number of items in the list
        """
        for i in range(index, len(self)):
            self.array[i] = self.array[i+1]

    def is_full(self):
        """ Returns true if the list is full
        :complexity: O(1)
        """
        return len(self) >= len(self.array)

    def index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item
        :raises ValueError: if item not in the list
        :complexity: O(Comp==) if item is first; Comp== is the BigO of ==
                     O(len(self)*Comp==) if item is last
        """
        for i in range(len(self)):
            if item == self[i]:
                return i
        raise ValueError("Item not in list")
    
    def delete_at_index(self, index: int) -> T:
        """ Moves self[j+1] to self[j] if j>index, returns old self[index]
        :pre: index is 0 <= index < len(self) checked by self.array[_]
        :complexity: O(len(self) - index)
        """
        if index < 0 or index > len(self):
            raise IndexError("Out of bounds")
        item = self.array[index]     
        self.length -= 1 
        self.__shuffle_left(index)
        return item

    def insert(self, index: int, item: T) -> None:
        """ Moves self[j] to self[j+1] if j>=index & sets self[index]=item
        :pre: index is 0 <= index <= len(self) checked by self.array[_]
        :complexity: O(len(self)-index) if no resizing needed, O(len(self)) otherwise
        """
        if self.is_full():
            raise Exception("List is full")
        self.__shuffle_right(index)
        self.array[index] = item
        self.length += 1 



class Node(Generic[T]): 
    """ Implementation of a generic Node class
    
    Attributes:
         item (T): the data to be stored by the node
         link (Node[T]): pointer to the next node

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.link = None


class LinkListIterator(Generic[T]): 
    def __init__(self, node: Node[T]) -> None:
        self.current = node

    def __iter__(self) -> 'LinkListIterator':
        return self
    
    def __next__(self) -> T:
        if self.current is not None:
            item = self.current.items
            self.current = self.current.link
            return item
        else:
            raise StopIteration         


class LinkList(List[T]): 
    """ Implementation of a generic list with linked nodes.
    
    Attributes:
         length (int): number of elements in the list (inherited)
         head (Node[T]): node at the head of the list
    """
    def __init__(self) -> None:
        """ Initialises self.length by calling its parent and 
        self.head as None, since the list is initially empty
        :complexity: O(1)
        """        
        List.__init__(self)
        self.head = None

    def __iter__(self) -> LinkListIterator[T]:
        """ Computes and returns an iterator for the current list
        :complexity: O(1)
        """        
        return LinkListIterator(self.head)

    def __setitem__(self, index: int, item: T) -> None:
        """ Sets the value of the element at position index to be item
        :see: #__get_node_at_index(index)
        """
        node_at_index = self.__get_node_at_index(index)
        node_at_index.item = item

    def __getitem__(self, index: int) -> T:
        """ Returns the value of the element at position index
        :see: #__get_node_at_index(index)
        """
        node_at_index = self.__get_node_at_index(index)
        return node_at_index.item 

    def is_full(self):
        """ Returns true if the list is full
        :complexity: O(1)
        """
        return False

    def __get_node_at_index(self, index: int) -> Node[T]:
        """ Returns the node in the list at position index
        :complexity: O(index)
        :pre: index is 0 <= index < len(self)
        """
        if 0 <= index and index < len(self):
            current = self.head
            for i in range(index):
                current = current.link
            return current
        else:
            raise ValueError("Index out of bounds")
            
    def insert(self, index: int, item: T) -> None:
        """ Moves self[j] to self[j+1] if j>=index & sets self[index]=item
        :pre: index is 0 <= index <= len(self), checked by __get_node_at_index
        :complexity: O(index) 
        """
        new_node = Node(item)
        if index == 0:
            new_node.link = self.head
            self.head = new_node
        else:
            previous_node = self.__get_node_at_index(index-1)
            new_node.link = previous_node.link
            previous_node.link = new_node
        self.length += 1

    def index(self, item: T) -> int:
        """ Returns the position of the first occurrence of item
        :raises ValueError: if item not in the list
        :complexity: O(Comp==) if item is first; Comp== is the BigO of ==
                     O(len(self)*Comp==) if item is last
        """
        current = self.head
        index = 0
        while current is not None and current.items != item:
            current = current.link
            index += 1
        if current is None:
            raise ValueError("Item is not in list")
        else:
            return index

    def delete_at_index(self, index: int) -> T:
        """ Moves self[j+1] to self[j] if j>index & returns old self[index]
        :pre: index is 0 <= index < len(self), checked by __get_node_at_index
        :complexity: O(index)
        """
        try:
            previous_node = self.__get_node_at_index(index-1)
        except ValueError as e:
            if self.is_empty(): 
                raise ValueError("List is empty")
            elif index == 0:
                item = self.head.items
                self.head = self.head.link
            else:
                raise e
        else:
            item = previous_node.link.items
            previous_node.link = previous_node.link.link
        self.length -= 1
        return item

    def delete_negative(self):
        """ Deletes all nodes with a negative item. 
        :complexity: O(len(self))
        """
        previous = self.head
        for _ in range(1,self.length): # delete negative nodes from index 1
            current = previous.link
            if current.items < 0:
                previous.link = current.link    # delete the node 
                self.length -= 1
            else:
                previous = current              # move previous along

        if self.length > 0 and self.head.items < 0: #check node at index 0
            self.head = self.head.link             # move the head 
            self.length -= 1

    def clear(self):
        """ Overrides the parent to set the head to None 
        :complexity: O(1) 
        """
        List.clear(self)
        self.head = None


class DataStructure(Enum):
     ARRAY = 1    
     LINK = 2    


class TestList(unittest.TestCase):
    """ Tests for the above class."""
    EMPTY = 0
    ROOMY = 5
    LARGE = 10

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]
        if test_list == DataStructure.ARRAY:
            self.lists = [ArrayList(self.LARGE) for i in range(len(self.lengths))]
        else:
            self.lists = [LinkList() for i in range(len(self.lengths))]
        for list, length in zip(self.lists, self.lengths):
            for i in range(length):
                list.append(i)
        self.empty_list = self.lists[0]
        self.roomy_list = self.lists[1]
        self.large_list = self.lists[2]
        #we build empty lists from clear.
        #this is an indirect way of testing if clear works!
        #(perhaps not the best)
        self.clear_list = self.lists[3]
        self.clear_list.clear()
        self.lengths[3] = 0
        self.lists[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.lists:
            s.clear()

    def test_init(self) -> None:
        self.assertTrue(self.empty_list.is_empty())
        self.assertEqual(len(self.empty_list), 0)
            
    def test_len(self):
        """ Tests the length of all lists created during setup."""
        for list, length in zip(self.lists, self.lengths):
            self.assertEqual(len(list), length)
            
    def test_is_empty_add(self):
        """ Tests lists that have been created empty/non-empty."""
        self.assertTrue(self.empty_list.is_empty())
        self.assertFalse(self.roomy_list.is_empty())
        self.assertFalse(self.large_list.is_empty())
    
    def test_is_empty_clear(self):
        """ Tests lists that have been cleared."""
        for list in self.lists:
            list.clear()
            self.assertTrue(list.is_empty())
            
    def test_is_empty_delete_at_index(self):
        """ Tests lists that have been created and then deleted completely."""
        for list in self.lists:
            #we empty the list
            for i in range(len(list)):
                self.assertEqual(list.delete_at_index(0), i)
            try:
                list.delete_at_index(-1)
            except:
                self.assertTrue(list.is_empty())
            
    def test_append_and_remove_item(self):
        for list in self.lists:
            nitems = self.ROOMY
            list.clear()
            for i in range(nitems):
                list.append(i)
            for i in range(nitems-1):
                list.remove(i)
                self.assertEqual(list[0],i+1)
            list.remove(nitems-1)
            self.assertTrue(list.is_empty())
            for i in range(nitems):
                list.append(i)
            for i in range(nitems-1,0,-1):
                list.remove(i)
                self.assertEqual(list[len(list)-1],i-1)
            list.remove(0)
            self.assertTrue(list.is_empty())
                
    def test_clear(self):
        for list in self.lists:
            list.clear()
            self.assertTrue(list.is_empty())


if __name__ == '__main__':
    test_list = DataStructure.ARRAY
    testtorun = TestList()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)

    test_list = DataStructure.LINK
    testtorun = TestList()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
