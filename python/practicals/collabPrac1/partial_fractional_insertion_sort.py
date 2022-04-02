from typing import List
from math import modf

def frac(x:float) -> float:
    """
    returns the fractional part of the input number.
    """
    return abs(modf(x)[0])

def partial_fractional_insertion_sort(the_list: List[float], start:int, end:int) -> None:
    """ Sorts (in place, by insertion) the element of the list according to their fractional part,
    between the starting index (included) and the end index (excluded).
    If start == end, then do nothing.
    (for example, the fractional part of 3.4 is .4)

    :pre: The list must not be None.
    :pre: 0 <= start <= end <= length of list
    :post: the list is sorted between start (included) and end (excluded)
    :post: the floats with the same fractional value have the same relative order in the_list before and after the call.
    :complexity: Best O(N) if the sublist is already sorted, worst O(N^2),
                 where N is the length of sublist.
    """
    #TODO write the function here.
def partial_fractional_insertion_sort(the_list: List[float], indexOne: int, indexTwo: int) -> None:
    assert not indexTwo<indexOne, "Index two is less than index one!"
    n = len(the_list)
    for mark in range(indexOne+1,indexTwo):
        temp = the_list[mark]
        i = mark - 1
        while i >= indexOne and frac(the_list[i]) < frac(temp):
            the_list[i+1] = the_list[i]
            i -= 1
        the_list[i+1] = temp
    assert len(the_list) == n, "The size of the list has changed!"
    return None

if __name__=="__main__":
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    partial_fractional_insertion_sort(the_list, 1, 7)
    print(the_list)

    the_list = []
    partial_fractional_insertion_sort(the_list, 0,0)
    print(the_list)

    the_list = [1, 0]
    partial_fractional_insertion_sort(the_list, 0,1)
    print(the_list)

    #TODO write more tests here
    the_list = [1, 0, 1.1, 2.5, 4.3, 7.6, 4.3, 9.4, 1.2, 4.3]
    partial_fractional_insertion_sort(the_list, 3,6)
    print(the_list)
