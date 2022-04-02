"""Unit Testing for Task B"""
__author__ = 'Graeme Gange'
__docformat__ = 'reStructuredText'
__modified__ = '19/05/2021'
__since__ = '19/05/2021'

import unittest
from avl import AVLTree, AVLTreeNode
from io import StringIO
import copy


# Helper methods, to construct trees directly.
def make_leaf(key):
    node = AVLTreeNode(key)
    node.height = 1
    return node


def make_node(key, left, right):
    node = AVLTreeNode(key)
    node.left = left
    node.right = right
    node.height = 1 + max(left.height, right.height)
    return node


def make_tree(root):
    tree = AVLTree()
    tree.root = root
    return tree


def nodes_equal(actual, expected):
    if actual is expected:
        return True
    if actual is None or expected is None:
        return False

    if actual.key != expected.key:
        return False
    return nodes_equal(actual.left, expected.left) and \
           nodes_equal(actual.right, expected.right)


def show_node(node):
    msg = StringIO()
    tree = AVLTree()
    tree.draw_aux(node, prefix='', final='', to=msg)
    msg.seek(0)
    return ''.join(msg.readlines())


# Now the actual tests
class TestTaskB(unittest.TestCase):
    def setUp(self) -> None:
        """ Used by our test cases """
        self.tree = make_tree(
            make_node(8,
                      make_node(120,
                                make_node(60,
                                          make_node(30,
                                                    make_leaf(9),
                                                    make_leaf(44)
                                                    ),
                                          make_leaf(11)
                                          ),
                                make_node(180,
                                          make_leaf(147),
                                          make_leaf(190)
                                          )
                                ),
                      make_leaf(200)
                      )
        )

    def test_get_height(self) -> None:
        """ Check correct height computations. """
        for (node, expected) in [
            (self.tree.root, 5),
            (self.tree.root.left, 4),
            (self.tree.root.left.right, 2)
        ]:
            height = self.tree.get_height(node)
            self.assertEqual(height, expected,
                             f'Expected height {expected} of node {node.key}, got {height} instead for tree:\n{show_node(node)}')

    def test_get_balance(self) -> None:
        """ Testing the computation of balance factor. """
        for (node, expected) in [
            (self.tree.root, -3),
            (self.tree.root.left, -1),
            (self.tree.root.left.right, 0)
        ]:
            balance = self.tree.get_balance(node)
            self.assertEqual(balance, expected,
                             f'For tree:\n{show_node(node)}Expected balance of {expected} for node {node.key}, got {balance} instead.')

    def test_right_rotate(self) -> None:
        """ Testing the result of right-rotate operations. """
        # We make copies to isolate issues with mutation.
        tree = copy.deepcopy(self.tree)
        for node in [
            self.tree.root,
            self.tree.root.left,
            self.tree.root.left.left
        ]:
            cpy = copy.deepcopy(node)
            expected = make_node(cpy.left.key, cpy.left.left, make_node(cpy.key, cpy.left.right, cpy.right))
            result = tree.right_rotate(node)
            self.assertTrue(nodes_equal(result, expected),
                            f'For right_rotate on:{show_node(node)}Expected:\n{show_node(expected)}\nGot: {show_node(result)}')
            # Now restore the original.
            tree = copy.deepcopy(self.tree)


if __name__ == '__main__':
    unittest.main()
