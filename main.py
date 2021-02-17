import sys
import unittest

from q1 import funnySort
from q2 import distantODDNumbers
from q3 import isAnagram
from q4 import highestSumList
from q5 import sumOfPrimes

class SetTestSolutions(unittest.TestCase):
    def test_funnySort(self):
        # standard example:
        assert funnySort([1, 7, 2, 3, 19, 5]) == [19, 7, 1, 2, 5, 3]
        # incorrect input:
        assert funnySort(1) == "Parameter must be an array."
        # string:
        assert funnySort("Hi") == "Parameter must be an array."
        # single-item array:
        assert funnySort([1]) == [1]
        # single-item floating point array:
        assert funnySort([1.0]) == [1]

    def test_distantODDNumbers(self):
        # standard example:
        assert distantODDNumbers([4, 3, 5, 2, 3, 8]) == [5, 8, 3, 2, 4, 3]
        assert distantODDNumbers([9, 2, 3, 3, 4]) == [3, 2, 3, 4, 9]
        # incorrect input:
        assert distantODDNumbers(1) == "Parameter must be an array."
        assert distantODDNumbers("hhhh") == "Parameter must be an array."

    def test_isAnagram(self):
        # standard example:
        assert isAnagram('zzcz', 'aaad', -1)  == True
        assert isAnagram('aaad', 'zzcz', -1)  == True
        assert isAnagram('aaad', 'xwuy', -1)  == False
        assert isAnagram('d', 'xwuy', 0)  == False
        # incorrect input:
        assert isAnagram(1, 'zzcz', -1)  == "First parameter must be a number."
        assert isAnagram('aaad', 1, -1)  == "Second parameter must be a number."
        assert isAnagram('aaad', 'aaad', "cat")  == "Third parameter must be a number."

    def test_highestSumList(self):
        array = [
                    [1, 0, 0, 0],
                    [2, 5, 0, 0],
                    [3, 2, 1, 0],
                    [1, 3, 2, 1]
                ]
        # standard example:
        assert highestSumList(array) == [1, 5, 2, 3]
        # incorrect input:
        assert highestSumList([1,2,2]) == "Input must be 2-D array."
        assert highestSumList("array") == "Input must be 2-D array."
        assert highestSumList(1) == "Input must be 2-D array."

    def test_sumOfPrimes(self):
        # standard example:
        assert sumOfPrimes(9) == [7,2]
        assert sumOfPrimes(6) == "NO SOLUTION based on the restrictions"
        assert sumOfPrimes(5) == [3,2]
        assert sumOfPrimes(10) == [5, 3, 2]

        # incorrect input:
        assert sumOfPrimes(1) == "Please enter an integer number larger than 1."
        assert sumOfPrimes(-1) == "Please enter an integer number larger than 1."

if __name__ == "__main__":
    # run tests.
    unittest.main()
