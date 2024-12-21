'''
Binary Search concept:
 Delete half of the elements at a time to get the answer.
  *Only works if its ordered.
  -log₂(n) tries.
'''


def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:    # "There's something to search?"
        mid = (begin + end) // 2    # Returns a integer for the central element.
        if array[mid] == item: # The answer is found.
            return mid
        if item < array[mid]: # The guess was too low.
            return binary_search(array, item, begin, mid-1) # Starts searching from the left.
        else: # The guess was too high.
            return binary_search(array, item, mid+1, end) # Starts searching from the right.
    return None # Item doesn't exist.

'''
-Let's suppose you have a list with 128 names and are doing a binary search.What is the maximum number of tries that you will take to find the wanted name?
    log₂(128) = 7 steps.

-Now, if you double the size of the list.What will be the maximum number of tries?
    128.2 = 256
    log₂(256) = 8 steps.
'''

