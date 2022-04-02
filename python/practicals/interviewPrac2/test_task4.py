"""
Testing file for Question 4 of Interview Prac 2

__author__ = "Maria Garcia de la Banda"
__edited__ = "Ben Di Stefano, Er Tian Ru"
"""

import unittest
from army import Archer, Soldier, Cavalry, Army
from battle import Battle


class TestTask4(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def tearDown(self):
        for item in self.verificationErrors:
            print(item)
        print("Number of Errors = " + str(len(self.verificationErrors)))

    def test___conduct_combat(self):
        # Assumes __assign_army is working correctly
        t1 = Army()
        t2 = Army()
        battle = Battle()
        formation = 0

        # Test if combat is conducted correctly and returns appropriate result for empty p1 army and all Archer p2 army
        t1._Army__assign_army("", 0, 0, 0, formation)
        t2._Army__assign_army("", 0, 10, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 2, "Gladiatorial 0,0,0 0,10,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for all Soldier p1 army and empty p2 army
        t1._Army__assign_army("", 10, 0, 0, formation)
        t2._Army__assign_army("", 0, 0, 0, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Gladiatorial 10,0,0 0,0,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for one cavalry p1 army
        # and one archer p2 army
        t1._Army__assign_army("", 0, 0, 1, formation)
        t2._Army__assign_army("", 0, 1, 0, formation)
        t1.force[0].gain_experience(1)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 1, "Gladiatorial 0,0,1 0,1,0 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Test if combat is conducted correctly and returns appropriate result for p1 and p2 army with the same units
        t1._Army__assign_army("", 1, 1, 1, formation)
        t2._Army__assign_army("", 1, 1, 1, formation)
        try:
            self.assertTrue(battle._Battle__conduct_combat(t1, t2, formation) == 0, "Gladiatorial 1,1,1 1,1,1 failed")
        except AssertionError as e:
            self.verificationErrors.append(str(e))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTask4)
    unittest.TextTestRunner(verbosity=0).run(suite)
