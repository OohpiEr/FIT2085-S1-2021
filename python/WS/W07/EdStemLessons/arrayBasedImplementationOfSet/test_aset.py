"""
    Unit test for ASet, implemented via inheritance from TestSet.
"""
from test_set import *
from aset import *

class TestASet(TestSet):

    @classmethod
    def setUpClass(cls):
        #TODO
        cls.SetType = ASet

    #TODO?

if __name__ == '__main__':
    testtorun = TestASet()
    suite = unittest.TestLoader().loadTestsFromModule(testtorun)
    unittest.TextTestRunner().run(suite)
