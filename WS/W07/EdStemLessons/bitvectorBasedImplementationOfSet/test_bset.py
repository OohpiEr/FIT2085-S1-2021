"""
    Unit test for BSet, implemented via inheritance from TestSet.
"""
from test_set import *
from bset import *

class TestBSet(TestSet):
    @classmethod
    def setUpClass(cls):
        # define the variable SetType
        # to be the class to test
        # e.g. cls.SetType = XYZ
        cls.SetType = BSet

if __name__ == '__main__':
    testtorun = TestBSet()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
