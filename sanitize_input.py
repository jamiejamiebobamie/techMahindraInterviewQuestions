# def sanitize(input, test):
#     try:
#         # cast the possible floating point number into an int
#         input = test(input)
#     except ValueError as ve:
#         return
#     except TypeError as te:
#         return
#     except AttributeError as ae:
#         return
#     return input

def sanitize(input, desired_type):
        return type(input) is type(desired_type)
    # try:
    #     # cast the possible floating point number into an int
    #     input = test(input)
    # except ValueError as ve:
    #     return
    # except TypeError as te:
    #     return
    # except AttributeError as ae:
    #     return
    # return input
