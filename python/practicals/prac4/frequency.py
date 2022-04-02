"""Frequency class and quicksort implementation """
__author__ = 'Brendon Taylor and Er Tian Ru'
__docformat__ = 'reStructuredText'
__modified__ = '30/05/2020'
__since__ = '22/05/2020'

from hash_table import LinearProbeHashTable
from dictionary import Dictionary
from list_adt import ArrayList
from enum import Enum
from typing import Tuple
# todo use this to get rid of punctuation
from string import punctuation
import sys

from referential_array import ArrayR


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    MISSPELT = 3


class Frequency:
    """ Implementation of Frequency class.

    Constants:
        DEFAULT_ENCODING = default encoding for opening files

    Attributes:
         hash_table (LinearProbeHashTable): KEY: word, VALUE: number of occurrence of word
         dictionary (Dictionary): Dictionary that read in "english_large.txt"
         max_word (Tuple(word, frequency)): word with the most number of occurrence and its frequency

    ArrayR cannot create empty arrays. So MIN_CAPCITY used to avoid this.
    """
    DEFAULT_ENCODING = 'utf-8'

    def __init__(self) -> None:
        """Initialises hash_table, max_word, and dictionary which reads in english_large.txt.

        :complexity: O(N) + O(K) where N is the table size and K is the number of lines in  "english_large.txt"
        """
        self.hash_table = LinearProbeHashTable(27183, 402221)
        self.dictionary = Dictionary(27183, 402221)
        self.dictionary.load_dictionary("english_large.txt")
        self.max_word = ()

    def add_file(self, filename: str) -> None:
        """Reads each word that exists in the dictionary from a file into hash_table.

        :param filename: name of the file (e.g. "test_file.txt")
        :complexity: O(N^2)
        """
        with open(filename, 'r', encoding=Frequency.DEFAULT_ENCODING) as file:
            for line in file:
                line = line.strip().lower()

                words = line.split()
                for word in words:
                    word = word.strip(punctuation)
                    if self.hash_table.__contains__(word):
                        self.hash_table.__setitem__(word, self.hash_table.__getitem__(word) + 1)
                    elif self.dictionary.find_word(word):
                        self.hash_table.__setitem__(word, 1)

                    try:
                        if len(self.max_word) == 0 or self.max_word[1] < self.hash_table.__getitem__(word):
                            self.max_word = (word, self.hash_table.__getitem__(word))
                    except KeyError:
                        pass

    def rarity(self, word: str) -> Rarity:
        """Returns the rarity score of a given word as an enumerated value.

        :param word: given word
        :complexity best: O(K) first position is empty
                          where K is the size of the word
        :complexity worst: O(K + N) when we've searched the entire hashtable
                           where N is the table_size
        """

        try:
            num_occurrence = self.hash_table.__getitem__(word.lower())
        except KeyError:
            rarity_score = Rarity.MISSPELT
        else:
            if num_occurrence >= self.max_word[1] / 100:
                rarity_score = Rarity.COMMON
            elif num_occurrence < self.max_word[1] / 1000:
                rarity_score = Rarity.RARE
            else:
                rarity_score = Rarity.UNCOMMON

        return rarity_score

    def ranking(self) -> ArrayList[tuple]:
        """ Returns an array list of the tuples (word, frequency) in hash_table sorted by their frequency in descending
        order.

        :complexity: O(K) + O(NlogN) where K is the table size of the hash table and N is the size of the array
        """
        array = ArrayList(2000)
        for word in self.hash_table.table:
            if word is not None:
                array.append(word)
        quick_sort(array)
        return array


def quick_sort(array: ArrayR) -> None:
    """ QuickSort public interface.

    :param array: the array to sort
    :complexity: O(NlogN)
    """
    start = 0
    end = len(array) - 1
    quick_sort_aux(array, start, end)


def quick_sort_aux(array: ArrayR, start: int, end: int) -> None:
    """ Actual implementation of QuickSort.
        Sorts a list of elements in-place in descending order.

    :param array: the array to sort
    :param start: index of the start of the section to sort
    :param end: index of last element of the section to sort
    :complexity: O(NlogN)
    """
    if start < end:
        boundary = partition(array, start, end)
        quick_sort_aux(array, start, boundary - 1)
        quick_sort_aux(array, boundary + 1, end)


def partition(array: ArrayR, start: int, end: int) -> int:
    """ Partitions a section of an array given by a starting index to an ending index.
    Selects a the middle element as the pivot and
        1. moves greater elements to the left
        2. moves smaller elements to the right
    Returns the position of the pivot element (boundary).

    :param array: the array to partition
    :param start: index of the start of the section to partition
    :param end: index of last element of the section to partition
    :complexity: O(N)
    """
    mid = (start + end) // 2
    pivot = array[mid]
    swap(array, start, mid)

    boundary = start
    for k in range(start + 1, end + 1):
        if array[k][1] >= pivot[1]:
            boundary += 1
            swap(array, k, boundary)

    swap(array, start, boundary)
    return boundary


def swap(array, i, j):
    """ swaps element at position i with element at position j in an array

    :param array: the array to swap
    :param i: index position of first element
    :param j: index position of second element
    :complexity: O(1)
    """
    array[i], array[j] = array[j], array[i]


def frequency_analysis() -> None:
    """ Creates an instance of class Frequency, adds 215-0.txt to it and generates the ranking list.
    It then prompts the user for the number of rankings to show and prints the rankings.
    """
    filename = "215-0.txt"

    frequency = Frequency()
    frequency.add_file(filename)
    rankings = frequency.ranking()
    while True:
        try:
            num_rankings = int(input("number of rankings: "))
        except ValueError:
            print("number of rankings must be an integer")
        else:
            output = ""
            for i in range(num_rankings):
                elem = rankings[i]
                if elem is not None:
                    output += "Ranking: {}, Word: {}, Frequency: {}, Rarity: {}\n".format(i + 1, elem[0], elem[1],
                                                                                          str(frequency.rarity(
                                                                                              elem[0]))[7:])
            print(output[:-1])
            break


if __name__ == '__main__':
    frequency_analysis()
