from typing import List

from indicator_greater_than import indicator_greater_than
from indicator_sublist import indicator_sublist

def pivot(the_list: List[float], pivot:float) -> List[float]:
    """ Creates a new list where all the elements smaller than 
    the value pivot are placed before the larger (or equal) elements.
    The relative order of the smaller elements is unchanged.
    The relative order of the larger elements is unchanged.

    :pre: The list must not be None.
    :post: the input list is not modified
    :complexity: Best and worst O(N) where N is the length of list.
    """
    #TODO
    assert the_list is not None, "The list must not be None"

    input_list = the_list.copy

    bool_list = indicator_greater_than(the_list, pivot)
    greater_pivot_sublist = indicator_sublist(the_list, bool_list)
    not_bool_list = [not elem for elem in bool_list]
    smaller_pivot_sublist = indicator_sublist(the_list, not_bool_list)
    return smaller_pivot_sublist + greater_pivot_sublist

    assert the_list == input_list, "the input list has been modified"


if __name__=="__main__": 
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    print(pivot(the_list, 2.5))
