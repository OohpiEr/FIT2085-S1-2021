from hash_table import LinearProbeHashTable
from typing import Tuple
import timeit
import csv


class Statistics:
    FILENAMES = ['english_small.txt', 'english_large.txt', 'french.txt']
    TABLESIZE = [250727, 402221, 1000081]
    HASHBASE = [1, 27183, 27183]

    def load_statistics(self, hash_base: int, table_size: int, filename: str, max_time: int) -> Tuple:
        """
        creates a new dictionary with hash_base and table_size and returns the
        tuple (words, time, conflict_count, probe_total, probe_max, rehash_count)
            where:
                words is the number of words added to the table
                time is the time taken for load_dictionary to complete if <= max_time and max_time otherwise
                The rest of the tuple elements are as in statistics above.
        """
        my_dictionary = Dictionary(hash_base, table_size)

        try:
            start_time = timeit.default_timer()
            words = my_dictionary.load_dictionary(filename, max_time)
        except TimeoutError:
            words = my_dictionary.hash_table.count
            time = max_time
        else:
            time = timeit.default_timer() - start_time

        return (words, time) + my_dictionary.hash_table.statistics()

    def table_load_statistics(self, max_time:int) -> None:
        with open('output_task2.csv', mode='w') as output_task2:
            output_task2_writer = csv.writer(output_task2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            output_task2_writer.writerow(['Hash Base', 'Table Size', 'Label', 'Filename', 'Words',
                                          'Time', 'Collisions', 'Probes', 'Probe Max', 'Rehash'])
            for hash_base in self.HASHBASE:
                for tb_size in self.TABLESIZE:
                    for filename in self.FILENAMES:
                        my_statistics = self.load_statistics(hash_base, tb_size, filename, max_time)
                        words = my_statistics[0]
                        time = my_statistics[1]
                        conflict_count = my_statistics[2]
                        probe_total = my_statistics[3]
                        probe_max = my_statistics[4]
                        rehash_count = my_statistics[5]

                        output_task2_writer.writerow([hash_base, tb_size, 'B = ' + str(hash_base) + 'TS = ' + str(tb_size),
                                                      filename, words, time, conflict_count, probe_total,
                                                      probe_max, rehash_count])


class Dictionary:
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
        start_time = timeit.default_timer()
        with open(filename) as file:
            count = 0
            for line in file:
                if time_limit is not None:
                    if (timeit.default_timer() - start_time) > time_limit:
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
    s = Statistics()
    s.table_load_statistics(10)
    menu(dictionary)
    # statistics = Statistics()
    # statistics.table_load_statistics(3)
    #
    # dictionary = Dictionary(31, 250727)
    # menu(dictionary)
