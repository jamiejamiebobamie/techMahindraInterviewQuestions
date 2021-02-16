import sys
from sanitize_input import sanitize

def distantODDNumbers(array):
    """
        Time complexity: ???
        Space complexity: ???
    """
    # sanitize the input to ensure it's an array.
    test = sanitize(unsorted_array, sorted)
    if not test:
        return "Parameter must be an array."

    # initialize a lookup dictionary of odd numbers and their indices.
        # odd_index : odd_number
    record_odds = {}
    for i in range(len(array)):
        if array[i] % 2:
            record_odds[i] = array[i]
    # calculate the bare minimum number of evens to separate odds
    required_evens = len(record_odds) - 1
    # calculate the number of evens
    even_count = len(array) - len(record_odds)
    # determine if there are enough even numbers to separate odd numbers
    if required_evens > even_count:
        return "Not enough evens to separate odds."
    # ensure that the last item of the array is an odd number as this is always
        # the case (as is the first item.)
    # initialize an array of all of the odd indices
    arr_record_odd_indices = list(record_odds.keys())
    # get the first odd_index of the array (this will be random.)
    odd_index = arr_record_odd_indices[0]
    # swap the last element of the array with the element at the odd index
    array[len(array) - 1], array[odd_index] = array[odd_index], array[len(array) - 1]
    # delete the entry from the record of odd indices / values
    del record_odds[odd_index]

    # determine the gap between consecutive odd numbers.
    gap = even_count // required_evens
    # initialize the count
    count = gap
    # iterate through the input array swapping the odd elements from their current
        # place into their required place, determined by the gap.
    for i in range(len(array)):
        # if the gap equals the count, it is time for an odd value.
        if gap == count:
            arr_record_odd_indices = list(record_odds.keys())
            odd_index = arr_record_odd_indices[0]
            array[i], array[odd_index] = array[odd_index], array[i]
            del record_odds[odd_index]
            count = 0
        else:
            count += 1
        # break early if no more odd values to swap.
        if not len(record_odds):
            break

    return array

if __name__ == "__main__":
    array = [int(string) for string in sys.argv[1:]]
    print(distantODDNumbers(array))
