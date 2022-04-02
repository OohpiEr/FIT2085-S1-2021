"""
Testing file for Question 3 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano"
__edited__ = "Er Tian Ru"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from unittest import mock


class TestTask3(unittest.TestCase):
    SINGLE = False

    def setUp(self):
        self.verificationErrors = []
        self.MaxDiff = None

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = " + str(len(self.verificationErrors)))

    ## 2021-04-21 - Removed residual '@mock.patch' tests.

    def test__correct_army_given(self):
        t1 = Army()

        # Test if a (low) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(1, 1, 1), msg="Stack test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if a (high) valid combination of unit values is accepted
        try:
            self.assertTrue(t1._Army__correct_army_given(5, 5, 5), msg="Stack test 5,5,5 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if an invalid combination of unit values is accepted
        try:
            self.assertFalse(t1._Army__correct_army_given(10, 10, 10), msg="Stack test 10,10,10 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test__str__(self):
        sold = "Soldier's life = 3 and experience = 0"
        arch = "Archer's life = 3 and experience = 0"
        cav = "Cavalry's life = 4 and experience = 0"
        t1 = Army()

        # Test if the string representation of the army matches expected output for low unit values
        t1._Army__assign_army("t1", 1, 1, 1, 0)
        try:
            self.assertEqual(str(t1.force), sold + "," + arch + "," + cav, msg="String test 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        sold = "Soldier's life = 3 and experience = 0"
        arch = "Archer's life = 3 and experience = 0"
        cav = "Cavalry's life = 4 and experience = 0"
        t2 = Army()

        # Test if the string representation of the army matches expected output for high unit values
        t2._Army__assign_army("t2", 2, 2, 2, 0)
        string = sold + "," + sold + "," + arch + "," + arch + "," + cav + "," + cav
        try:
            self.assertEqual(str(t2), string, msg="String test 2,2,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if the string representation of the army matches expected output for empty army
        t3 = Army()
        try:
            self.assertEqual(str(t3), "", msg="String test 2,2,2 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask3)
    unittest.TextTestRunner(verbosity=0).run(suite)
