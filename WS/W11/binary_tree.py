""" Binary Tree ADT.
Defines a Binary Tree with linked nodes.
Each node only contains a single item.
"""
__author__ = "Brendon Taylor"
__docformat__ = 'reStructuredText'

from typing import Callable, TypeVar, Generic
T = TypeVar('T')


class BinaryTreeNode(Generic[T]):
    def __init__(self, item: T = None) -> None:
        """
        Initialises the node with an optional item
        and sets the left and right pointers to None
        :complexity: O(1)
        """
        self.item = item
        self.left = None
        self.right = None

    def __str__(self) -> str:
        """
        Returns the string representation of a node
        :complexity: O(N) where N is the size of the item
        """
        return str(self.item)


class BinaryTree(Generic[T]):
    def __init__(self) -> None:
        """
        Initialises an empty Binary Tree
        :complexity: O(1)
        """
        self.root = None

    def __len__(self) -> int:
        """
        Calculates the length of the tree recursively
        O(N) where N is number of nodes in the tree
        """
        return self.len_aux(self.root)

    def len_aux(self, current: T) -> int:
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def is_empty(self) -> bool:
        """
        Checks to see if the tree is empty
        :complexity: O(1)
        """
        return self.root is None

    def preorder(self, f: Callable) -> None:
        """
        Preforms a pre-order traversal of the tree
        O(N) where N is number of nodes in the tree
        """
        self.preorder_aux(self.root, f)

    def preorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:  # if not a base case
            f(current)
            self.preorder_aux(current.left, f)
            self.preorder_aux(current.right, f)

    def inorder(self, f: Callable) -> None:
        """
        Preforms a in-order traversal of the tree
        O(N) where N is number of nodes in the tree
        """
        self.inorder_aux(self.root, f)

    def inorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:  # if not a base case
            self.inorder_aux(current.left, f)
            f(current.item)
            self.inorder_aux(current.right, f)

    def postorder(self, f: Callable) -> None:
        """
        Preforms a post-order traversal of the tree
        O(N) where N is number of nodes in the tree
        """
        self.postorder_aux(self.root, f)

    def postorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:  # if not a base case
            self.postorder_aux(current.left, f)
            self.postorder_aux(current.right, f)
            f(current.item)
