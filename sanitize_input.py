def sanitize(input, test, error_message):
    try:
        # cast the possible floating point number into an int
        input = test(input)
    except ValueError as ve:
        print(error_message)
        return
    except TypeError as te:
        print(error_message)
        return
    return input
