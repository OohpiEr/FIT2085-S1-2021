""" AVL Tree implemented on top of the standard BST. """

__author__ = 'Alexey Ignatiev'
__docformat__ = 'reStructuredText'

from bst import BinarySearchTree
from typing import TypeVar, Generic
from node import AVLTreeNode, TreeNode

K = TypeVar('K')
I = TypeVar('I')


class AVLTree(BinarySearchTree, Generic[K, I]):
    """ Self-balancing binary search tree using rebalancing by sub-tree
        rotations of Adelson-Velsky and Landis (AVL).
    """

    def __init__(self) -> None:
        """
            Initialises an empty Binary Search Tree
            :complexity: O(1)
        """

        BinarySearchTree.__init__(self)

    def get_height(self, current: AVLTreeNode) -> int:
        """
            Get the height of a node. Return current.height if current is
            not None. Otherwise, return 0.
            :complexity: O(1)
        """

        return current.height if current is not None else 0

    def get_balance(self, current: AVLTreeNode) -> int:
        """
            Compute the balance factor for the current sub-tree as the value
            (right.height - left.height). If current is None, return 0.
            :complexity: O(1)
        """

        return 0 if current is None else (self.get_height(current.right) - self.get_height(current.left))

    def insert_aux(self, current: AVLTreeNode, key: K, item: I) -> AVLTreeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert
            it. After insertion, performs sub-tree rotation whenever it becomes
            unbalanced.
        """

        if current is None:  # base case: at the leaf
            current = TreeNode(key, item)
            self.length += 1
        elif key < current.key:
            current.left = self.insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError('Inserting duplicate item')
        current.height = max(self.get_height(current.left), self.get_height(current.right)) + 1
        new_current = self.rebalance(current)
        return new_current

    def delete_aux(self, current: AVLTreeNode, key: K) -> AVLTreeNode:
        """
            Attempts to delete an item from the tree, it uses the Key to
            determine the node to delete. After deletion,
            performs sub-tree rotation whenever it becomes unbalanced.
        """

        if current is None:  # key not found
            raise ValueError('Deleting non-existent item')
        elif key < current.key:
            current.left = self.delete_aux(current.left, key)
        elif key > current.key:
            current.right = self.delete_aux(current.right, key)
        else:  # we found our key => do actual deletion
            if self.is_leaf(current):
                self.length -= 1
                return None
            elif current.left is None:
                self.length -= 1
                return current.right
            elif current.right is None:
                self.length -= 1
                return current.left

            # general case => find a successor
            succ = self.get_successor(current)
            current.key = succ.key
            current.item = succ.item
            current.right = self.delete_aux(current.right, succ.key)

        current.height = max(self.get_height(current.left), self.get_height(current.right)) + 1
        new_current = self.rebalance(current)
        return new_current

    def right_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform right rotation of the sub-tree.
            Left child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            Example:

                       current                                child
                      /       \                              /     \
                  child       r-tree     --------->     l-tree     current
                 /     \                                           /     \
            l-tree     center                                 center     r-tree

            :complexity: O(1)
        """
        child = current.left
        center = child.right
        child.right = current
        current.left = center
        current.height = max(self.get_height(current.left),self.get_height(current.right)) + 1
        child.height = max(self.get_height(child.left),self.get_height(child.right)) + 1
        return child

    def left_rotate(self, current: AVLTreeNode) -> AVLTreeNode:
        """
            Perform left rotation of the sub-tree.
            Right child of the current node, i.e. of the root of the target
            sub-tree, should become the new root of the sub-tree.
            Example:

                 current                                       child
                /       \                                      /   \
            l-tree     child           -------->        current     r-tree
                      /     \                           /     \
                 center     r-tree                 l-tree     center

            :complexity: O(1)
        """
        r_child = current.right
        c_tree = r_child.left

        # rotation
        r_child.left = current
        current.right = c_tree

        # Update heights
        current.height = 1 + max(self.get_height(current.left), self.get_height(current.right))
        r_child.height = 1 + max(self.get_height(r_child.left), self.get_height(r_child.right))

        # returns the smallest node (root)
        return r_child

    def rebalance(self, current: AVLTreeNode) -> AVLTreeNode:
        """ Compute the balance of the current node.
            Do rebalancing of the sub-tree of this node if necessary.
            Rebalancing should be done either by:
            - one left rotate
            - one right rotate
            - a combination of left + right rotate
            - a combination of right + left rotate
        """
        if self.get_balance(current) >= 2:
            child = current.right

            if self.get_height(child.left) > self.get_height(child.right):
                current.right = self.right_rotate(child)

            return self.left_rotate(current)

        if self.get_balance(current) <= -2:
            child = current.left

            if self.get_height(child.right) > self.get_height(child.left):
                current.left = self.left_rotate(child)

            return self.right_rotate(current)

        return current