from typing import List


def get_minimum(the_list: List[int]) -> int:
    """Computes the minimum element of a given list of integers.
    :pre: the list has at least one element
    """ 
    min_item = the_list[0]
    for i in range(1, len(the_list)):
        item = the_list[i]
        if min_item > item:
            min_item = item
    return min_item 


def main() -> None:
    my_list = [2, 4, -1]
    print("The minimum element in this list is " + str(get_minimum(my_list)))


main()