""" Binary Search Tree ADT.
Defines a Binary Search Tree with linked nodes.
Each node only contains a single item.
"""
__author__ = "Brendon Taylor"
__docformat__ = 'reStructuredText'

from typing import TypeVar, Generic
T = TypeVar('T')


class BinarySearchTreeNode(Generic[T]):
    def __init__(self, item: T = None) -> None:
        """
        Initialises the node with a key and optional item
        and sets the left and right pointers to None
        :complexity: O(1)
        """
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns the string representation of a node
        :complexity: O(N) where N is the size of the item
        """
        return str(self.item)


class BinarySearchTree(Generic[T]):
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

    def __contains__(self, key: T) -> bool:
        """
        Checks to see if the key is in the BST
        :complexity: see __getitem__(self, key: T) -> T
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: T) -> T:
        """
        Attempts to get an item in the tree, it uses the Key to attempt to find it
        :complexity best: O(CompK) finds the item in the root of the tree
        :complexity worst: O(CompK * D) item is not found, where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        return self.getitem_aux(self.root, key)

    def getitem_aux(self, current: BinarySearchTreeNode, key: T) -> T:
        if current is None:  # base case: empty
            raise KeyError("Key not found")
        elif key == current.item:  # base case: found
            return current.item
        elif key < current.item:
            return self.getitem_aux(current.left, key)
        else:  # key > current.key
            return self.getitem_aux(current.right, key)

    def __setitem__(self, key: T, item: T) -> None:
        self.root = self.insert_aux(self.root, key)

    def insert_aux(self, current: BinarySearchTreeNode, key: T) -> BinarySearchTreeNode:
        """
        Attempts to insert an item into the tree, it uses the Key to insert it
        :complexity best: O(CompK) inserts the item at the root.
        :complexity worst: O(CompK * D) inserting at the bottom of the tree
        where D is the depth of the tree
        CompK is the complexity of comparing the keys
        """
        if current is None:  # base case: at the leaf
            current = BinarySearchTreeNode(key)
        elif key < current.item:
            current.left = self.insert_aux(current.left, key)
        elif key > current.item:
            current.right = self.insert_aux(current.right, key)
        else:  # key == current.key
            raise ValueError("Inserting duplicate item")
        return current

    def get_max(self) -> T:
        """
        Get the maximum element in the BST
        :complexity best: O(1) root is maximum.
        :complexity worst: O(D) when the depth is equal to the number of nodes in the tree (single line)
        where D is the depth of the tree
        """
        if self.root is None:
            raise ValueError("Heap is empty")
        elif self.root.right is None:  # root has the max
            temp = self.root.item
            self.root = self.root.left  # delete root
            return temp
        else:
            return self.get_max_aux(self.root.right, self.root)

    def get_max_aux(self, current, parent) -> T:
        if current.right is None:  # base case: at max
            parent.right = current.left
            return current.item
        else:
            return self.get_max_aux(current.right, current)
