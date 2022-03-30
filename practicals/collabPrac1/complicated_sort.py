from typing import List
from pivot import pivot
from bicriteria_sort import bicriteria_sort


def complicated_sort(the_list: List[float]) -> List[float]:
    """ Sorts a list of floats by non-decreasing order of integer parts, and as a tie-breaker,
     by non-increasing order of their fractional part.

    :raises TypeError: if the list is None.
    :complexity: Best O(N) if the sublist is already sorted, worst O(N^2),
                 where N is the length of sublist.
    """
    # TODO
    if the_list is None:
        raise TypeError("the list is None")

    if len(the_list) == 0:
        pivot_num =0
    else:
        pivot_num = sum(the_list) / len(the_list)

    new_list = pivot(the_list, pivot_num)
    pivot_index = 0
    for i in range(0, len(new_list) - 1):
        if new_list[i] <= pivot_num:
            pivot_index = i
    bicriteria_sort(new_list, 0, pivot_index+1)
    bicriteria_sort(new_list, pivot_index+1, len(new_list))
    return new_list


if __name__ == "__main__":
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    print(complicated_sort(the_list))
