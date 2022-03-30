from typing import List


def partial_integral_insertion_sort(the_list: List[float], start: int, end: int) -> None:
    """ Sorts (in place, by insertion) the element of the list according to their integral part,
    between the starting index (included) and the end index (excluded).
    If start == end, then do nothing.
    (for example, the integral part of 3.4 is 3.)

    :pre: The list must not be None.
    :pre: 0 <= start <= end <= length of list
    :post: the list is sorted between start (included) and end (excluded)
    :post: the floats with the same integral value have the same relative order in the_list before and after the call.
    :complexity: Best O(N) if the sublist is already sorted, worst O(N^2),
                 where N is the length of sublist.
    """
    # TODO write the function here.

    assert the_list is not None, "The list must not be None"
    assert 0 <= start <= end <= len(the_list), "0 <= start <= end <= length of list"

    for mark in range(start, end):
        temp = the_list[mark]
        i = mark - 1
        while int(the_list[i]) > int(temp) and i >= start:
            the_list[i + 1] = the_list[i]
            i -= 1
        the_list[i + 1] = temp


if __name__ == "__main__":
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    partial_integral_insertion_sort(the_list, 1, 7)
    print(the_list)

    the_list = []
    partial_integral_insertion_sort(the_list, 0, 0)
    print(the_list)

    the_list = [1, 0]
    partial_integral_insertion_sort(the_list, 0, 1)
    print(the_list)

    # TODO write more tests here
    the_list = [-1, 3.0, 2.4, 2.5, 1]
    partial_integral_insertion_sort(the_list, -1, 1)
    print(the_list)

