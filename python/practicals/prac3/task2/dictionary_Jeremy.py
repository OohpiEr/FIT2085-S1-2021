""" Module containing the Dictionary and Statistics class
Dictionary models a dictionary using a linear probe hash table
Statistics contains methods to analyse runtime statistics of a Dictionary instance

__author__ = "Jeremy Yoon"

"""

from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit
import csv


class Statistics:
    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> Tuple:
        """
        Creates a new dictionary with hash_base and table_size and returns a tuple containing the number of words added to the table, the time taken for load_dictionary to complete if <= max_time and max_time otherwise, the total number of conflicts, the sum of all the probe chain lengths, the length of the longest probe chain, and the number of times rehash has been called.
        :complexity: O(N), where N is the number of lines in the file.
        """

        dictionary = Dictionary(hash_base, table_size)
        try:
            starttime = timeit.default_timer()
            words = dictionary.load_dictionary(filename, max_time)
            time = timeit.default_timer() - starttime
        except TimeoutError:
            words = dictionary.hash_table.count
            time = max_time
        return (words, time) + dictionary.hash_table.statistics()

    def table_load_statistics(self, max_time: int) -> None:
        """
        For each possible combination of values in the lists below, uses load_statistics to time how long it takes for load_dictionary to run. Outputs to output_task2.csv the statistics of each combination.
        :complexity: O(N), where N is the size of the largest file
        """
        b = [1, 27183, 250726]
        TABLESIZE = [250727, 402221, 1000081]
        Filename = ["english_large.txt", "english_small.txt", "french.txt"]
        with open("output_task2.csv", mode='w') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(
                ['File Name', 'Table Size', 'Hash Base', 'Number of Words', 'Total Conflicts', 'Probe Chain Length Sum',
                 'Longest Probe Chain Length', 'Number of Rehashes', 'Time Taken'])
            for hash_base in b:
                for table_size in TABLESIZE:
                    for file_name in Filename:
                        statistics = self.load_statistics(hash_base, table_size, file_name, max_time)
                        writer.writerow([file_name, table_size, hash_base, statistics[0], statistics[2], statistics[3],
                                         statistics[4], statistics[5], statistics[1]])


class Dictionary:
    def __init__(self, hash_base: int, table_size: int) -> None:
        """
        creates a new Hash Table with the given hash base and initial table size,
        and uses it to initialise the instance variable self.hash_table.
        :complexity: O(N), where N is the table size
        """
        self.hash_table = LinearProbeHashTable(hash_base, table_size)

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """
        1. reads a file filename containing one word per line, and
        2. adds each word to self.hash_table with integer 1 as the associated data, and
        3. returns the number of words successfully read into the hash table.
        4. If time_limit is specified and loading the dictionary
        exceedstime_limit seconds, a TimeoutError is immediately raised.
        :complexity: O(N), where N is the number of lines in the file
        """
        starttime = timeit.default_timer()
        with open(filename) as file:
            for line in file:
                self.hash_table.insert(line.strip(), 1)
                if time_limit is not None and timeit.default_timer() - starttime > time_limit:
                    raise TimeoutError

        return self.hash_table.count

    def add_word(self, word: str) -> None:
        """which adds the given word to the hash table with integer 1
        as the associated data.
        :complexity: Best case: O(1). Worst case: O(N), where N is the size of the Hash Table
        """
        if str != "":
            self.hash_table.insert(word.lower(), 1)

    def find_word(self, word: str) -> bool:
        """which returns True if the word is in the hash table and
                         False otherwise.
        :complexity: Best case: O(1). Worst case: O(N), where N is the size of the Hash Table
        """
        if str != "":
            return self.hash_table.__contains__(word.lower())

    def delete_word(self, word: str) -> None:
        """
        which deletes the given word from the hash table.
        :complexity: Best case: O(1). Worst case: O(N), where N is the size of the Hash Table
        """
        if str != "":
            self.hash_table.__delitem__(word.lower())


def process_option(dictionary: Dictionary, method_name: str) -> None:
    """ Helper code for processing menu options."""
    if method_name == 'read_file':
        filename = input('Enter filename: ')
        try:
            dictionary.load_dictionary(filename)
            print('Successfully read file')
        except FileNotFoundError as e:
            print(e)
    else:
        word = input('Enter word: ')
        if method_name == 'add_word':
            dictionary.add_word(word)
            try:
                dictionary.add_word(word)
                print('[{}] {}'.format(word, 'Successfully added'))
            except IndexError as e:
                print('[{}] {}'.format(word, e))
        elif method_name == 'find_word':
            if dictionary.find_word(word):
                print('[{}] {}'.format(word, 'Found in dictionary'))
            else:
                print('[{}] {}'.format(word, 'Not found in dictionary'))
        elif method_name == 'delete_word':
            try:
                dictionary.delete_word(word)
                print('[{}] {}'.format(word, 'Deleted from dictionary'))
            except KeyError:
                print('[{}] {}'.format(word, 'Not found in dictionary'))


def menu(dictionary: Dictionary):
    """ Wrapper for using the dictionary. """
    option = None
    menu_options = {'read_file': 'Read File',
                    'add_word': 'Add Word',
                    'find_word': 'Find Word',
                    'delete_word': 'Delete Word',
                    'exit': 'Exit'}

    exit_option = list(menu_options.keys()).index('exit') + 1

    while option != exit_option:
        print('---------------------')
        opt = 1
        for menu_option in menu_options.values():
            print('{}. {}'.format(opt, menu_option))
            opt += 1
        print('---------------------')
        try:
            option = int(input("Enter option: "))
            if option < 1 or option > exit_option:
                raise ValueError('Option must be between 1 and ' + str(exit_option))
        except ValueError as e:
            print('[{}] {}'.format('menu', e))
        else:
            if option != exit_option:
                process_option(dictionary, list(menu_options.keys())[option - 1])
    print("---------------------")


if __name__ == '__main__':
    dictionary = Dictionary(31, 250727)
    s = Statistics()
    s.table_load_statistics(10)
    menu(dictionary)
