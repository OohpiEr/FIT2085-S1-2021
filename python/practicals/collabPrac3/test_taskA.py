"""Unit Testing for Task A"""
__author__ = 'Graeme Gange, Alexey Ignatiev'
__docformat__ = 'reStructuredText'
__modified__ = '19/05/2021'
__since__ = '19/05/2021'

# from avl import AVLTree
from avl import AVLTree
from bst import BinarySearchTree
import copy
from io import StringIO
from node import AVLTreeNode, TreeNode
import unittest


# Helper methods (AVL)
def make_aleaf(key):
    return AVLTreeNode(key)


def make_anode(key, left, right):
    node = AVLTreeNode(key)
    node.left = left
    node.right = right
    node.height = 1 + max(left.height, right.height)
    return node


def make_atree(root):
    tree = AVLTree()
    tree.root = root
    return tree


# Helper methods (BST)
def make_bleaf(key):
    return TreeNode(key)


def make_bnode(key, left, right):
    node = TreeNode(key)
    node.left = left
    node.right = right
    return node


def make_btree(root):
    tree = BinarySearchTree()
    tree.root = root
    return tree


# Helper methods (common)
def nodes_equal(actual, expected):
    if actual is expected:
        return True
    if actual is None or expected is None:
        return False

    if actual.key != expected.key:
        return False
    return nodes_equal(actual.left, expected.left) and \
           nodes_equal(actual.right, expected.right)


def get_left(node):
    return node.left


def get_right(node):
    return node.right


class TestTaskABST(unittest.TestCase):

    def setUp(self) -> None:
        """ Used by our test cases """
        self.tree = make_btree(
            make_bnode(8,
                       make_bleaf(5),
                       make_bnode(12,
                                  make_bnode(10,
                                             make_bleaf(9),
                                             make_bleaf(11)
                                             ),
                                  make_bnode(18,
                                             make_bleaf(16),
                                             make_bnode(122,
                                                        make_bleaf(50),
                                                        make_bleaf(200)
                                                        )
                                             )
                                  )
                       )
        )

    def test_get_minimal(self) -> None:
        """ Testing minimal node computation. """
        for root, node in [
            (self.tree.root, self.tree.root.left),
            (self.tree.root.right, self.tree.root.right.left.left),
            (self.tree.root.right.right, self.tree.root.right.right.left),
            (self.tree.root.right.right.right, self.tree.root.right.right.right.left),
            (self.tree.root.right.right.right.left, self.tree.root.right.right.right.left),
        ]:
            # making copies
            tcopy = copy.deepcopy(self.tree)
            rcopy = copy.deepcopy(root)
            ncopy = copy.deepcopy(node)

            # checking
            got = tcopy.get_minimal(root)
            res = nodes_equal(got, node)

            # message:
            msg = StringIO()
            print('Initial tree is:', file=msg)
            self.tree.draw(to=msg)

            print('Getting successor for node {0}'.format(root), file=msg)
            print('Got:', got, file=msg)
            print('Expected:', node, file=msg)

            msg.seek(0)

            self.assertTrue(res, msg=''.join(msg.readlines()))

    def test_get_successor(self) -> None:
        """ Testing successor computation. """
        for root, node in [
            (self.tree.root, self.tree.root.right.left.left),
            (self.tree.root.right, self.tree.root.right.right.left),
            (self.tree.root.right.right, self.tree.root.right.right.right.left),
            (self.tree.root.right.right.right.left, None),
            (self.tree.root.right.right.right.right, None)
        ]:
            # making copies
            tcopy = copy.deepcopy(self.tree)
            rcopy = copy.deepcopy(root)
            ncopy = copy.deepcopy(node)

            # checking
            got = tcopy.get_successor(root)
            res = nodes_equal(got, node)

            # message:
            msg = StringIO()
            print('Initial tree is:', file=msg)
            self.tree.draw(to=msg)

            print('Getting successor for node {0}'.format(root), file=msg)
            print('Got:', got, file=msg)
            print('Expected:', node, file=msg)

            msg.seek(0)

            self.assertTrue(res, msg=''.join(msg.readlines()))


class TestTaskAAVL(unittest.TestCase):

    def setUp(self) -> None:
        """ Used by our test cases """
        self.tree = make_atree(
            make_anode(8,
                       make_aleaf(5),
                       make_anode(12,
                                  make_anode(10,
                                             make_aleaf(9),
                                             make_aleaf(11)
                                             ),
                                  make_anode(18,
                                             make_aleaf(16),
                                             make_anode(122,
                                                        make_aleaf(50),
                                                        make_aleaf(200)
                                                        )
                                             )
                                  )
                       )
        )

    def test_left_rotate(self) -> None:
        """ Testing left rotation. """
        torig = copy.deepcopy(self.tree)
        for (tree, node) in [
            (torig, get_right(torig.root)),
            (torig, get_right(get_right(torig.root))),
            (torig, torig.root)
        ]:
            tcopy = copy.deepcopy(tree)
            ncopy = copy.deepcopy(node)

            expected = make_anode(
                ncopy.right.key,
                make_anode(
                    ncopy.key,
                    ncopy.left,
                    ncopy.right.left
                ),
                ncopy.right.right
            )

            got = tcopy.left_rotate(node)
            res = nodes_equal(got, expected)

            # message:
            msg = StringIO()
            print('Initial tree is:', file=msg)
            self.tree.draw(to=msg)

            print('Applying left rotation to node {0}'.format(node.key), file=msg)
            print('Got sub-tree:', file=msg)
            make_atree(got).draw(to=msg)

            print('Expected sub-tree:', file=msg)
            make_atree(expected).draw(to=msg)

            msg.seek(0)

            self.assertTrue(res, msg=''.join(msg.readlines()))


if __name__ == '__main__':
    unittest.main()
