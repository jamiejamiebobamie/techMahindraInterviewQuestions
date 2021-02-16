def highestSumList(lst):
    """
        Time complexity: ???
        Space complexity: ???
    """
    max_sums = {}
    def recursion(row,col,indices):
        # the bounds on this may be wrong...
        if row == len(lst) or col == len(lst[0])-1:
            _sum = sum(indices)
            _indices = tuple(indices)
            max_sums[_indices] = _sum
        else:
            deep_copy = []
            for index in indices:
                deep_copy.append(index)
            deep_copy.append(lst[row][col])
            recursion(row+1,col,deep_copy)

            deep_copy = []
            for index in indices:
                deep_copy.append(index)
            deep_copy.append(lst[row][col+1])
            recursion(row+1,col+1,deep_copy)
        return

    recursion(0,0,[])

    _max_v = float("-inf")
    _max_k = None

    for k,v in max_sums.items():
        if v > _max_v:
            _max_k = k
            _max_v = v

    return _max_k
