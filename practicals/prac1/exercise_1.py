""" Menu to read items into a list , print the list , print the number of items, remove the last item and reverse it."""

from typing import List, TypeVar  # imports some types you may need

T = TypeVar('T')  # creates a type variable which you will need


def print_menu() -> None:
    print('\nMenu:')
    print('1. append')
    print('2. reverse')
    print('3. print')
    print('4. last')
    print('5. count')
    print('6. quit')


def reverse(my_list: List[T]) -> None:
    length = len(my_list)
    for i in range(length // 2):
        temp = my_list[i]
        my_list[i] = my_list[length - i - 1]
        my_list[length - i - 1] = temp


def last(my_list: List[T]) -> List[T]:
    """returns a new list with the last item removed, after printing the item"""
    print(my_list[-1])
    temp_list = []
    for i in range(len(my_list) - 1):
        temp_list.append(my_list[i])
    return temp_list


def count(my_list: List[T]) -> None:
    """prints the number of times a given value appears in the list"""
    item = input('Item? ')
    counter = 0
    for i in my_list:
        if i == item:
            counter += 1
    print(counter)


def main() -> None:
    my_list = []
    selected_quit = False
    input_line = None

    while not selected_quit:
        print_menu()
        command = int(input('\nEnter command: '))
        if command == 1:
            item = input('Item? ')
            my_list.append(item)
        elif command == 2:
            reverse(my_list)
        elif command == 3:
            print(my_list)
        elif command == 4:
            my_list = last(my_list)
        elif command == 5:
            count(my_list)
        elif command == 6:
            selected_quit = True


if __name__ == '__main__':
    main()