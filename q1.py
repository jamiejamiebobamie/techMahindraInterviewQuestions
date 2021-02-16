import sys
from sanitize_input import sanitize

def funnySort(unsorted_array):
    """
        Time complexity: O(nlogn)
        Space complexity: O(n)
    """

    # sanitize the input to ensure it's an iterable.
    sanitize(unsorted_array, len, "Parameter must be an array or string.")

    # ensure correct parameters
    # try:
    #     len(unsorted_array)
    # except TypeError as te:
    #     print("Parameter must be an array or string.")
    #     return

    # ensure array has at least two elements
    if len(unsorted_array) < 2:
        return unsorted_array

    # sort the array
    sorted_array = sorted(unsorted_array)

    # initialize the indices
    i, j, k, l = 0, 1, len(sorted_array) - 2, len(sorted_array) - 1

    # initialize return array for "funnysorted" items
    funnySorted_array = []

    # iterate through the sorted_array from the front and the back, and append
        # the items in correct order
    while j <= l:

        # biggest element
        funnySorted_array.append(sorted_array[l])
        # second biggest element
        funnySorted_array.append(sorted_array[k])

        # test to ensure the same element(s) aren't added twice.
        if j != l:
            # smallest element
            funnySorted_array.append(sorted_array[i])
            # second smallest element
            funnySorted_array.append(sorted_array[j])

        # increment/decrement the indices by two
        i+=2
        j+=2
        k-=2
        l-=2

    # some funky stuff is happening...
        # wrong output: [1,2,3,4,5]
        # wrong output: [6, 7, 8, 10, 11, 12, 13]
        # need better element checking with i,j,k,l

    # if sorted_array is odd, add the middle element
        # of the sorted_array as it was excluded
    # if len(sorted_array) % 2:
    #     middle_index = len(sorted_array)//2
    #     funnySorted_array.append(sorted_array[middle_index])


    return funnySorted_array

if __name__ == "__main__":
    unsorted_array = [int(string) for string in sys.argv[1:]]
    print(funnySort(unsorted_array))
