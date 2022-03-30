from typing import List, TypeVar
T = TypeVar('T')

def indicator_sublist(the_list: List[T], indicator: List[bool]) -> List[T]:
    """ Takes a list and outputs a new sublist of its elements, based on the indicator list.
    More precisely, an element at index i in the_list belongs to the returned sublist
    if and only if indicator[i]=True. Furthermore, the elements in the sublist
    should have the same relative order as in the_list.

    :pre: the_list and indicator must not be None and have the same size
    :post: the input list is not modified
    :post: the elements in the sublist should have the same relative order as in the_list.
    :complexity: Best and worst O(N) where N is the length of list.
    """
    #TODO write the function here.
    n = len(the_list)
    assert len(indicator) == n, "The two lists have different lengths!"
    newList = []
    for i in range(n):
        if(indicator[i]):
            newList.append(the_list[i])
    assert len(newList) <= n, "The new list is bigger than the provided list!"
    return newList
    pass

if __name__=="__main__":
    the_list = [3.4, 2, 1.6, 1.4, 3.2, 3.8, 2.2, 0.5]
    indicator = [True, False, False, False, True, True, False, False]
    print(indicator_sublist(the_list, indicator))

    the_list = []
    indicator = []
    print(indicator_sublist(the_list, indicator))

    the_list = [True]
    indicator = [False]
    print(indicator_sublist(the_list, indicator))

    the_list = [False]
    indicator = [True]
    print(indicator_sublist(the_list, indicator))

    #TODO write more tests here
    the_list = ["I", "am", "not", "a", "STEGOSAUROUS"]
    indicator = [True, True, False, True, True]
    print(indicator_sublist(the_list, indicator))
