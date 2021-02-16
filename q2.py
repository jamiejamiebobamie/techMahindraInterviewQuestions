def distantODDNumbers(array):
    """
        Time complexity: ???
        Space complexity: ???
    """
    record_odds = {}
    for i in range(len(array)):
        if array[i] % 2:
            record_odds[i] = array[i]

    required_evens = len(record_odds) - 1
    even_count = len(array) - len(record_odds)
    if required_evens > even_count:
        return
    gap = even_count // required_evens
    count = gap
    arr_record_odd_indices = list(record_odds.keys())
    odd_index = arr_record_odd_indices[0]
    array[len(array) - 1], array[odd_index] = array[odd_index], array[len(array) - 1]
    del record_odds[odd_index]

    for i in range(len(array)):
        if gap == count:
            arr_record_odd_indices = list(record_odds.keys())
            odd_index = arr_record_odd_indices[0]
            array[i], array[odd_index] = array[odd_index], array[i]
            del record_odds[odd_index]
            count = 0
        else:
            count += 1
        if not len(record_odds):
            break

    return array
