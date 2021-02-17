import sys
import copy
import random
from sanitize_input import sanitize

def sumOfPrimes(number):
    """
        Time complexity: O(n^2)
        Space complexity: O(n^2)

        Please do not use on numbers larger than 850. It takes too long.
    """

    # helper function.
    def build_primes(n):
        for i in range(3,n+1):
            not_divisible = True
            # only test odds
            if i % 2:
                # iterate through all of the currently added primes
                for _prime in _primes:
                    if not i % _prime:
                        not_divisible = False
                        break
                # if no _prime could evenly divide it, it's a new prime!
                if not_divisible:
                    _primes.append(i)

    # initialize a set of solutions.
    solutions = set()

    # we have a sorted list of primes.
    # at each call to this function, either add the prime
        # at the end of this list (the largest one) to the list of primes
        # we're summing. or don't
    def add_primes(remaining_primes, _current_sums):
        # only one solution is required.
        if len(solutions):
            return
        # if the sum of the current list of primes sums to the number,
            # we've found a solution.
        if number == sum(_current_sums):
            solutions.add(tuple(_current_sums))
        # if the list of primes too choose from is empty, there is no solution.
        if not len(remaining_primes):
            return
        # if the sum of the numbers in _current_sums is larger than the number
        if number < sum(_current_sums):
            return

        # we need deep copies otherwise mutiple stack frames would be
            # operating on the same object
        deep_copy_remaining_primes = copy.deepcopy(remaining_primes)
        deep_copy_current_sums = copy.deepcopy(_current_sums)

        # pop the last item
        last_item = deep_copy_remaining_primes.pop()

        # do not add the last_item to the sum list
        add_primes(deep_copy_remaining_primes, deep_copy_current_sums)

        # add the last_item to the sum list
        deep_copy_current_sums.append(last_item)
        add_primes(deep_copy_remaining_primes, deep_copy_current_sums)

    # sanitize the input to ensure it's a number.
    test = sanitize(number, 1)
    if not test:
        return "Parameter must be a number."

    # the lowest prime number is 2.
    if number < 2:
        return "Please enter an integer number larger than 1."

    # initialize a set of primes.
    _primes = [2]
    # build the set.
    build_primes(number)

    sorted_primes = _primes
    # build the set / solve.
    add_primes(sorted_primes, [])

    # return a single solution from the solution set otherwise return no solution.
    return list(list(solutions)[0]) if len(solutions) else "NO SOLUTION based on the restrictions"

if __name__ == "__main__":
    number = int(sys.argv[1])
    print(sumOfPrimes(number))
