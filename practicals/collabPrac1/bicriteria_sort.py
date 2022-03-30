from typing import List
from partial_integral_insertion_sort import partial_integral_insertion_sort
from partial_fractional_insertion_sort import frac, partial_fractional_insertion_sort


def bicriteria_sort(the_list: List[float], start: int, end: int) -> None:
    """ Sorts a list of floats between index start (included) and index end (excluded)
     by non-decreasing order of integer parts, and as a tie-breaker,
     by non-increasing order of their fractional part.

    :pre: The list must not be None.
    :complexity: Best O(N) if the sublist is already sorted, worst O(N^2),
                 where N is the length of sublist.
    """
    #TODO
    assert the_list is not None, "The list must not be None"

    partial_fractional_insertion_sort(the_list, start, end)
    partial_integral_insertion_sort(the_list, start, end)


if __name__=="__main__": 
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    bicriteria_sort(the_list, 1, 7)
    print(the_list)
