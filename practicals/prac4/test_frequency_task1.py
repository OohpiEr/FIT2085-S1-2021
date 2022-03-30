"""Unit Testing for Task 1 and 2"""
__author__ = 'Brendon Taylor and Er Tian Ru'
__docformat__ = 'reStructuredText'
__modified__ = '30/05/2020'
__since__ = '22/05/2020'

import unittest
import sys
from hash_table import LinearProbeHashTable
from frequency import Frequency, Rarity


class TestFrequency(unittest.TestCase):
    TEST_WORDS = [("TEST_WORD_COMMON", 30, Rarity.COMMON), ("TEST_WORD_RARE", 2, Rarity.RARE), ("TEST_WORD_UNCOMMON", 3, Rarity.UNCOMMON)]
    TEST_WORD_MISSPELT = ("TEST_WORD_MISSPELLED", None, Rarity.MISSPELT)
    TEST_WORD_MAX = "TEST_WORD_MAX"
    TEST_WORD_MAX_OCCURENCE = 3000

    def setUp(self) -> None:
        self.frequency = Frequency()

    def test_init(self) -> None:
        self.assertEqual(type(self.frequency.hash_table), LinearProbeHashTable)
        self.assertEqual(self.frequency.dictionary.find_word('test'), 1)

    def test_add_file(self) -> None:
        # test for add_file

        # test if hashtable is not empty
        self.frequency.add_file("215-0.txt")
        self.assertFalse(self.frequency.hash_table.is_empty())

        # test if number of occurrence is correct for the word "the"
        self.assertEqual(334, self.frequency.hash_table.__getitem__("the"),
                         msg="number of occurence of words do not match")

    def test_rarity(self) -> None:
        # test if rarity is working correctly for all cases
        self.frequency.max_word = (self.TEST_WORD_MAX, self.TEST_WORD_MAX_OCCURENCE)

        # test for COMMON, UNCOMMON and RARE
        for test_word in self.TEST_WORDS:
            self.frequency.hash_table.insert(test_word[0].lower(), test_word[1])
            self.assertEqual(test_word[2], self.frequency.rarity(test_word[0]), msg="error in " + test_word[0])

        # test for MISSPELT
        self.assertEqual(self.TEST_WORD_MISSPELT[2], self.frequency.rarity(self.TEST_WORD_MISSPELT[0]),
                         msg="error in " + self.TEST_WORD_MISSPELT[0])


if __name__ == '__main__':
    unittest.main()
