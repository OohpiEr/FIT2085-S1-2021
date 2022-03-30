""" Binary Search Tree ADT.
Defines a Binary Search Tree with linked nodes.
Each node contains a key and item.
"""
__author__ = "Brendon Taylor"
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
from list import LinkList
from stack import LinkStack
K = TypeVar('K')
I = TypeVar('I')


class BinarySearchTreeNode(Generic[K, I]):
    def __init__(self, key: K, item: I = None) -> None:
        """
        Initialises the node with a key and optional item
        and sets the left and right pointers to None
        :complexity: O(1)
        """
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns the string representation of a node
        :complexity: O(N) where N is the size of the item
        """
        return " (" + str(self.key) + ", " + str(self.item) + " ) "


class BSTPreOrderIterator:
    def __init__(self, root: BinarySearchTreeNode[K, I]) -> None:
        """
        Initialises a pre-order iterator
        The stack contains only the root element at the start
        """
        self.stack = LinkStack()
        self.stack.push(root)

    def __iter__(self) -> 'BSTPreOrderIterator':
        return self

    def __next__(self) -> (K, I):
        """
        Gets the next item in the pre-order traversal
        :complexity: O(1)
        """
        if self.stack.is_empty():
            raise StopIteration
        current = self.stack.pop()

        if current.right is not None:
            self.stack.push(current.right)
        if current.left is not None:
            self.stack.push(current.left)

        return current.items


class BinarySearchTree(Generic[K, I]):
    def __init__(self) -> None:
        """
        Initialises an empty Binary Search Tree
        :complexity: O(1)
        """
        self.root = None

    def is_empty(self) -> bool:
        """
        Checks to see if the bst is empty
        :complexity: O(1)
        """
        return self.root is None

    def __contains__(self, key: K) -> bool:
        """
        Checks to see if the key is in the BST
        :complexity: see __getitem__(self, key: K) -> (K, I)
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> (K, I):
        """
        Attempts to get an item in the tree, it uses the Key to attempt to find it
        :complexity best: O(CompK) finds the item in the root of the tree
        :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        return self.getitem_aux(self.root, key)

    def __iter__(self) -> BSTPreOrderIterator:
        return BSTPreOrderIterator(self.root)

    def getitem_aux(self, current: BinarySearchTreeNode, key: K) -> (K, I):
        if current is None:  # base case: empty
            raise KeyError("Key not found")
        elif key == current.key:  # base case: found
            return (current.key, current.item)
        elif key < current.key:
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            return self.getitem_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    def insert_aux(self, current: BinarySearchTreeNode, key: K, item: I) -> BinarySearchTreeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it
        :complexity best: O(CompK) inserts the item at the root.
        :complexity worst: O(CompK * D) inserting at the bottom of the tree
        where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = BinarySearchTreeNode(key, item)
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError("Inserting duplicate item")
        return current

    def get_leaves(self) -> LinkList:
        """
        Retrieves all the items that are leaf nodes
        :complexity: O(N) where N is the number of nodes in the BST
        """
        a_list = LinkList(len(self))
        self.get_leaves_aux(self.root, a_list)
        return a_list

    def is_leaf(self, current: BinarySearchTreeNode) -> bool:
        return current.left is None and current.right is None

    def get_leaves_aux(self, current: BinarySearchTreeNode, a_list: LinkList) -> None:
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.get_leaves_aux(current.left, a_list)
                self.get_leaves_aux(current.right, a_list)
