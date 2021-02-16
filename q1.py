import sys
from sanitize_input import sanitize

def funnySort(unsorted_array):
    """
        Time complexity: O(nlogn)
        Space complexity: O(n)
    """

    # sanitize the input to ensure it's an array.
    test = sanitize(unsorted_array, [])
    if not test:
        return "Parameter must be an array."

    sorted_array = sorted(unsorted_array)
    # ensure array has at least two elements
    if len(sorted_array) < 2:
        return sorted_array

    # initialize the indices
    i, j, k, l = 0, 1, len(sorted_array) - 2, len(sorted_array) - 1

    # initialize return array for "funnysorted" items
    funnySorted_array = []

    # iterate through the sorted_array from the front and the back, and append
        # the items in correct order.
    while j <= l:
        # biggest element
        if len(funnySorted_array) < len(sorted_array):
            funnySorted_array.append(sorted_array[l])
        # second biggest element
        if len(funnySorted_array) < len(sorted_array):
            funnySorted_array.append(sorted_array[k])
        # smallest element
        if len(funnySorted_array) < len(sorted_array):
            funnySorted_array.append(sorted_array[i])
        # second smallest element
        if len(funnySorted_array) < len(sorted_array):
            funnySorted_array.append(sorted_array[j])

        # increment/decrement the indices by two
        i+=2
        j+=2
        k-=2
        l-=2

    return funnySorted_array

if __name__ == "__main__":
    unsorted_array = [int(string) for string in sys.argv[1:]]
    print(funnySort(unsorted_array))
