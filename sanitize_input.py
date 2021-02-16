def sanitize(input, test):
    try:
        # cast the possible floating point number into an int
        input = test(input)
    except ValueError as ve:
        return
    except TypeError as te:
        return
    return input
