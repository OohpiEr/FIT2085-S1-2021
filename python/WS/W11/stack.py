""" Stack ADT and an array implementation.

Defines a generic abstract stack with the usual methods, and implements 
a stack using arrays. Also defines UnitTests for the class.
"""
__author__ = "Maria Garcia de la Banda, modified by Brendon Taylor"
__docformat__ = 'reStructuredText'

import unittest
from abc import ABC, abstractmethod 
from enum import Enum
from typing import Generic
from referential_array import ArrayR, T


class Stack(ABC, Generic[T]):
    def __init__(self) -> None:
        self.length = 0

    @abstractmethod
    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack."""
        pass

    @abstractmethod
    def pop(self) -> T:
        """ Pops an element from the top of the stack."""
        pass

    @abstractmethod
    def peek(self) -> T:
        """ Pops the element at the top of the stack."""
        pass

    def __len__(self) -> int:
        """ Returns the number of elements in the stack."""
        return self.length

    def is_empty(self) -> bool:
        """ True if the stack is empty. """
        return len(self) == 0

    @abstractmethod
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed. """
        pass

    def clear(self):
        """ Clears all elements from the stack. """
        self.length = 0


class ArrayStack(Stack[T]):
    """ Implementation of a stack with arrays.
    
    Attributes:
         length (int): number of elements in the stack (inherited)
         array (ArrayR[T]): array storing the elements of the queue

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """
    MIN_CAPACITY = 1 

    def __init__(self, max_capacity: int) -> None:
        """ Initialises the length and the array with the given capacity.
            If max_capacity is 0, the array is created with MIN_CAPACITY.
        """
        Stack.__init__(self)
        self.array = ArrayR(max(self.MIN_CAPACITY, max_capacity))
        
    def is_full(self) -> bool:
        """ True if the stack is full and no element can be pushed.
        :complexity: O(1)
        """
        return len(self) == len(self.array)

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack.
        :pre: stack is not full
        :complexity: O(1)
        :raises Exception: if the stack is full
        """
        if self.is_full():
            raise Exception("Stack is full")
        self.array[len(self)] = item
        self.length += 1

    def pop(self) -> T:
        """ Pops the element at the top of the stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        self.length -= 1
        return self.array[self.length]

    def peek(self) -> T:
        """ Returns the element at the top, without popping it from stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.array[self.length-1]
 
    def __str__(self) -> str:
        """Computes a string from the stack item - top to bottom.
        :complexity: O(N) where N is the size of the stack
        """
        length = len(self)
        if length > 0:
            output = str(self.array[length-1])
            for i in range(length-2, -1, -1):
                output += "," + str(self.array[i])
        else:
            output = ""
        return output


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


class LinkStack(Stack[T]):
    """ Implementation of a stack with linked nodes.

    Attributes:
         length (int): number of elements in the stack (inherited)
    """

    def __init__(self, _=None) -> None:
        Stack.__init__(self)
        self.top = None

    def clear(self) -> None:
        """" Resets the stack
        :complexity: O(1)
        """
        super().clear()
        self.top = None

    def is_empty(self) -> bool:
        """ Returns whether the stack is empty
        :complexity: O(1)
        """
        return self.top is None

    def is_full(self) -> bool:
        """ Returns whether the stack is full
        :complexity: O(1)
        """
        return False

    def push(self, item: T) -> None:
        """ Pushes an element to the top of the stack.
        :complexity: O(1)
        """
        new_node = Node(item)
        new_node.link = self.top
        self.top = new_node
        self.length += 1

    def pop(self) -> T:
        """ Pops the element at the top of the stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")

        item = self.top.item
        self.top = self.top.link
        self.length -= 1
        return item

    def peek(self) -> T:
        """ Returns the element at the top, without popping it from stack.
        :pre: stack is not empty
        :complexity: O(1)
        :raises Exception: if the stack is empty
        """
        if self.is_empty(self):
            raise Exception("Stack is empty")
        return self.top.item

    def __str__(self) -> str:
        """Computes a string from the stack item - top to bottom.
        :complexity: O(N) where N is the size of the stack
        """
        current = self.top
        output = ''
        while current is not None:
            if output != '':
                output += ', '
            output += str(current.item)
            current = current.link

        return output

class DataStructure(Enum):
    ARRAY = 1
    LINK = 2


class TestStack(unittest.TestCase):
    """ Tests for the above class."""
    EMPTY = 0
    ROOMY = 5
    LARGE = 10
    CAPACITY = 20

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]
        self.stacks = [ArrayStack(self.CAPACITY) for i in range(len(self.lengths))]

        if test_list == DataStructure.ARRAY:
            self.stacks = [ArrayStack(self.CAPACITY) for i in range(len(self.lengths))]
        else:
            self.stacks = [LinkStack() for i in range(len(self.lengths))]

        for stack, length in zip(self.stacks, self.lengths):
            for i in range(length):
                stack.push(i)
        self.empty_stack = self.stacks[0]
        self.roomy_stack = self.stacks[1]
        self.large_stack = self.stacks[2]
        #we build empty stacks from clear.
        #this is an indirect way of testing if clear works!
        #(perhaps not the best)
        self.clear_stack = self.stacks[3]
        self.clear_stack.clear()
        self.lengths[3] = 0
        self.stacks[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.stacks:
            s.clear()

    def test_init(self):
        self.assertTrue(self.empty_stack.is_empty())
        self.assertEqual(len(self.empty_stack), 0)
            
    def test_len(self):
        """ Tests the length of all stacks created during setup."""
        for stack, length in zip(self.stacks, self.lengths):
            self.assertEqual(len(stack), length)
            
    def test_is_empty_add(self):
        """ Tests stacks that have been created empty/non-empty."""
        self.assertTrue(self.empty_stack.is_empty())
        self.assertFalse(self.roomy_stack.is_empty())
        self.assertFalse(self.large_stack.is_empty())
    
    def test_is_empty_clear(self):
        """ Tests stacks that have been cleared."""
        for stack in self.stacks:
            stack.clear()
            self.assertTrue(stack.is_empty())
            
    def test_is_empty_pop(self):
        """ Tests stacks that have been popped completely."""
        for stack in self.stacks:
            #we empty the stack
            try:
                while True:
                    was_empty = stack.is_empty()
                    stack.pop()
                    #if we have popped without raising an assertion,
                    #then the stack was not empty.
                    self.assertFalse(was_empty)
            except:
                self.assertTrue(stack.is_empty())
            
    def test_is_full_add(self):
        """ Tests stacks that have been created not full."""
        self.assertFalse(self.empty_stack.is_full())
        self.assertFalse(self.roomy_stack.is_full())
        self.assertFalse(self.large_stack.is_full())
        
    def test_push_and_pop(self):
        for stack in self.stacks:
            nitem = self.ROOMY
            for i in range(nitem):
                stack.push(i)
            for i in range(nitem-1, -1, -1):
                self.assertEqual(stack.pop(), i)
                
    def test_clear(self):
        for stack in self.stacks:
            stack.clear()
            self.assertEqual(len(stack), 0)
            self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    test_list = DataStructure.ARRAY
    testtorun = TestStack()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)

    test_list = DataStructure.LINK
    testtorun = TestStack()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
