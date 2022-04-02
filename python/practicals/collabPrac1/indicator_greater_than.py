from typing import List


def indicator_greater_than(the_list: List[float], reference: float) -> List[bool]:
    """ Finds the elements of the given list which are greater than
    the given reference value and return a list of booleans.

    :pre: The list must not be None.
    :post: the input list is not modified
    :complexity: Best and worst O(N) where N is the length of list.
    """
    assert the_list is not None, "The list must not be None"

    # TODO write the function here.\
    temp = []
    for n in the_list:
        temp.append(n >= reference)
    return temp
    pass


if __name__ == "__main__":
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    print(indicator_greater_than(the_list, 2.5))

    the_list = []
    print(indicator_greater_than(the_list, 2.5))

    the_list = [1, 0]
    print(indicator_greater_than(the_list, 1))

    # TODO write more tests here

