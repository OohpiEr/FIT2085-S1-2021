from hash_table import LinearProbeHashTable
from typing import Tuple
from referential_array import ArrayR
import timeit


class Statistics:
    # TODO
    pass


class Dictionary():
    def __init__(self, hash_base: int, table_size: int) -> None:
        """
        creates a new Hash Table with the given hash base and initial table size,
        and uses it to initialise the instance variable self.hash_table.
        """
        assert(table_size > 0)
        self.hash_table = LinearProbeHashTable(hash_base, table_size)

    def load_dictionary(self, filename: str, time_limit: int = None) -> int:
        """
        1. reads a file filename containing one word per line, and
        2. adds each word to self.hash_table with integer 1 as the associated data, and
        3. returns the number of words successfully read into the hash table.
        4. If time_limit is specified and loading the dictionary
        exceedstime_limit seconds, a TimeoutError is immediately raised.
        """
        starttime = timeit.default_timer()
        with open(filename) as file:
            count = 0
            for line in file:
                if (time_limit is not None):
                    if (timeit.default_timer() - starttime) > time_limit:
                        raise TimeoutError
                self.add_word(line.rstrip())
                count += 1
            return count

    def add_word(self, word: str) -> None:
        """which adds the given word to the hash table with integer 1
        as the associated data.
        """
        self.hash_table.insert(word.lower(), 1)

    def find_word(self, word: str) -> bool:
        """which returns True if the word is in the hash table and
                         False otherwise.
        """
        try:
            self.hash_table.__getitem__(word.lower())
        except KeyError:
            return False
        else:
            return True

    def delete_word(self, word: str) -> None:
        """
        which deletes the given word from the hash table.
        """
        self.hash_table.__delitem__(word.lower())


def process_option(dictionary : Dictionary, method_name: str) -> None:
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


def menu(dictionary : Dictionary):
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
    menu(dictionary)
