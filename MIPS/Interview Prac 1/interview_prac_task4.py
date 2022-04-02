from typing import List


def bubble_sort(the_list: List[int]) -> None:
    n = len(the_list)   # assigns the size of the_list to n
    for a in range(n-1):    # loops through number of traversals
        for i in range(n-1):    # loops through each element in the_list
            item = the_list[i]  # item = current element
            item_to_right = the_list[i+1]   # item_to_right = next element
            if item > item_to_right:    # if item > item_to_right, swap them
                the_list[i] = item_to_right  # item_to_right now located at index i 
                the_list[i+1] = item  # item now located at index i+1 


def main() -> None:
    """ Calls bubble_sort() and prints each item in the newly sorted list """
    the_list = [4, -2, 6, 7]
    bubble_sort(the_list)

    for i in range(len(the_list)):
        # Print the item without a newline character
        print(the_list[i], end='')
        print(' ', end='')
    print()


main()