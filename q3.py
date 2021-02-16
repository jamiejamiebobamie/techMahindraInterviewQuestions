def isAnagram(a,b,x):
    """
        Time complexity: ???
        Space complexity: ???
    """
    # normalize x to be a number between 0 and 25
    if x < 0:
        if x > -27:
            x = 26 + x
        else:
            x %= 26
    elif x > 25:
        x %= 26

    alpha_lookup = {i : letter for i,letter in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
    index_lookup = {letter : i for i,letter in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}

    shifted_a = []
    for letter in a:
        index = index_lookup[letter]
        shifted_letter = alpha_lookup[index]
        shifted_a.append(shifted_letter)

    shifted_b = []
    for letter in b:
        index = index_lookup[letter]
        shifted_letter = alpha_lookup[index]
        shifted_b.append(shifted_letter)


    sorted_array_a = sorted(list(a))
    sorted_array_b = sorted(list(b))
    shifted_sorted_array_a = sorted(shifted_a)
    shifted_sorted_array_b = sorted(shifted_b)

    return True if (shifted_sorted_array_a == sorted_array_b
                    or sorted_array_a == shifted_sorted_array_b
                    or shifted_sorted_array_a == shifted_sorted_array_b) else False
