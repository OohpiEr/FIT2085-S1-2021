"""
    Unit test for classes that implement the Set ADT.
    The class TestSet is also abstract.
"""
import unittest
from abc import ABC, abstractmethod

class TestSet(ABC, unittest.TestCase):

    @classmethod
    @abstractmethod
    def setUpClass(cls):
        #define the variable SetType
        #to be the class to test
        #e.g. cls.SetType = XYZ
        pass

    def setUp(self):
        """
        Creates two sets with non-contiguous integer values.
        This uses add and remove, so they should not be used 
        to test add and remove!
        """
        self.capacity = 20
        self.s1 = self.SetType(self.capacity)
        self.s2 = self.SetType(self.capacity)
        self.in_s1 = set([3, 5, 6, 7, 10, 15, 16])
        self.in_s2 = set([5, 8, 9, 10, 15, 17])
        self.myset_pythonset_pairs = [(self.s1, self.in_s1), (self.s2, self.in_s2)]

        for the_set, the_items in self.myset_pythonset_pairs:
            for i in range(1, self.capacity):
                the_set.add(i)
            for i in range(1, self.capacity):
                if i not in the_items:
                    the_set.remove(i)

    def test_init(self):
        s = self.SetType(5)
        self.assertTrue(s.is_empty())
        self.assertEqual(len(s), 0)

    def test_len(self):
        s = self.SetType(10)
        for i in range(1, 8):
            s.add(i)
        self.assertEqual(len(s), 7)

    def test_is_empty(self):
        s = self.SetType(10)
        self.assertTrue(s.is_empty())
        s.add(1)
        self.assertFalse(s.is_empty())

    def test_clear(self):
        capacity = 10
        s = self.SetType(capacity)
        self.assertEqual(len(s), 0)
        s.clear()
        self.assertEqual(len(s), 0)
        s.add(2)
        s.clear()
        self.assertEqual(len(s), 0)
        for i in range(1, capacity):
            s.add(i)
        s.clear()
        self.assertEqual(len(s), 0)

    def test_contains(self):
        for the_set, the_items in self.myset_pythonset_pairs:
            for i in range(1, self.capacity):
                if i in the_items:
                    self.assertTrue(i in the_set)
                else:
                    self.assertFalse(i in the_set, "{} is actually in {}".format(i, the_set))

    def test_add(self):
        m = set(range(1, 8))
        s = self.SetType(10)
        for i in range(1, 8):
            s.add(i)
        for i in m:
            self.assertTrue(i in s)
        #we check that adding duplicates doesn't do anything
        size = len(s)
        for i in range(1, 8):
            s.add(i)
            self.assertEqual(size,len(s))

    def test_remove(self):
        s = self.SetType(10)
        for i in range(1, 7):
            s.add(i)
        for i in range(1, 4):
            s.remove(i)
        for i in range(4, 7):
            self.assertTrue(i in s)
        for i in range(1, 4):
            self.assertFalse(i in s)

    def test_union(self):
        truth = self.in_s1.union(self.in_s2)
        for s3 in [self.s1.union(self.s2), self.s2.union(self.s1)]:
            self.assertEqual(len(s3), len(truth))
            for i in range(1, self.capacity):
                if i in truth:
                    self.assertTrue(i in s3)
                else:
                    self.assertFalse(i in s3)

    def test_intersection(self):
        truth = self.in_s1.intersection(self.in_s2)
        for s3 in [self.s1.intersection(self.s2), self.s2.intersection(self.s1)]:
            self.assertEqual(len(s3), len(truth))
            for i in range(1, self.capacity):
                if i in truth:
                    self.assertTrue(i in s3)
                else:
                    self.assertFalse(i in s3)

    def test_difference(self):
        for truth, s3 in [\
         (self.in_s1.difference(self.in_s2), self.s1.difference(self.s2)),\
         ( self.in_s2.difference(self.in_s1), self.s2.difference(self.s1))]:
            self.assertEqual(len(s3), len(truth))
            for i in range(1, self.capacity):
                if i in truth:
                    self.assertTrue(i in s3)
                else:
                    self.assertFalse(i in s3)
