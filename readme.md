INSTRUCTIONS:
=============
1- Feel free to answer the questions in any of the following languages:
Java, C++, C, Python, JavaScript etc.

2- Imagine the methods you are implementing are going to be used by the world. Make sure you throw the right exceptions when necessary, and handle the edge cases.

3- Signature of the methods are given in Java. Feel free to convert the signature to your programming language of your choice, but make sure not to add anything extra

4- Feel free to use the Standard Libraries that come with the language of choice, and nothing more. (e.g. 'numpy' is not a standard Python library, but 're' is), Avoid Using Collections in Java for sorting and other questions.

5- We are NOT looking for the most efficient algorithm. Something that would return within reasonable time is good.

6- We are NOT looking for all the perfect and complete answers. However make sure that you are doing all this by yourself. There will be 3 more rounds of interview, including one onsite with similar questions. (DO NOT CHEAT)

7- Please provide the time complexity of your solution in terms of Big-O in a comment on top of your method

8- Please make sure your code compiles and runs. Provide test case to demonstrate correctness.


Question 1
==========

given a list of numbers, for example:
1, 7, 2, 3, 19, 5

if you sort them (ascending order) they will look like:
1, 2, 3, 5, 7, 19

however we want to sort them in a "funny" way, where the sort order is like:
largest number,  second largest, smallest number, second smallest, Third largest, fourth largest, third smallest, fourth smallest…
For the above example the funny sort will look like:
19, 7, 1, 2, 5, 3

Implement a method that gets a list of numbers, and returns a funny sorted list. The Java signature would look like:
List<Integer> funnySort(List<Integer> unsorted) {...}

=============================================================================
Question 2
==========

We have an array of Integers. We want to reorder the elements in-place to have ODD numbers as far from each other as possible (i.e. we want to maximize the minimum distance between any two even numbers in the list). Note that we do not want to create a second array, and would like this to happen in the original array, in-place.

For example:
[4, 3, 5, 2, 3, 8]
We can re-order the elements:
[3, 4, 5, 2, 8, 3]

or for the following list:
[9, 2, 3, 3, 4]
we can re-order to have:
[9, 2, 3, 4, 3]


Java Signature:

List<Integer> distantODDNumbers(List<Integer>) { /* return the same original array (with the modification) that is passed  to the method*/ }

=============================================================================

Question 3
==========

Def 1- two strings are anagrams if they have the exact same number of repetions for each letter.

for example:
  1- 'aaab' and 'abaa' are anagrams (a repeated 3 times and b repeated one time in each string)
  2- 'sdsd' and 'ssdd' are anagrams (s repeated 2 times and d repeated two times in each string)
  3- 'xxxa' and 'xxxx' are not anagrams

Def 2- for a given number x, here is a couple of examples of how the letters in a string are shifted by x characters:

  given the positive number x=4:
  a b c d e f g ... z
  a becomes e (4 letters after a)
  z becomes d (4 letters after z)
  d becomes h (4 letters after d)

  given the negative number x=-3:
  a b c d e f g ... z
  z becomes w (going 3 letters back from z)
  a becomes x (going 3 letters back from a)
  g becomes d (going 3 letters back from g)

Def 3- isAnagram(“Jonathan Smith”, “Mith Than Jonas”, 0) returns TRUE

Given two strings, and a number x indicating the number of letters to be shifted, find out if one of the strings is the shifted anagram of the other. Assume we only receive small letters (a to z) in the input. assume the two strings only include letters a to z, all small letters.


for example given 'aaad' and 'zzcz' and x = -1 the two strings are shifted anagrams, because if you first shift the characters to left by 1 in 'aaad', you get 'zzzc', and 'zzzc' and 'zzcz' are anagrams.

It should work regardless of the order two strings are passed in,
i.e. isAnagram('zzcz', 'aaad', -1) returns TRUE
also isAnagram('aaad', 'zzcz', -1) returns TRUE

here is the method signature if Java (x is the shift value as is mentioned in Def 2)

boolean isAnagram(String a, String b, int x) {...}


=============================================================================

Question 4
==========
1
2 5
3 2 1
1 3 2 1

Imagine you have a list of numbers like above (Size of first row is 1, and size of each row is size of previous row + 1). You should start from top and pick one number from each row. if you have picked the nth number from a row,
then you can ONLY pick nth or nth+1 number from the next row. From all the possible solutions, find the one that has the highest sum of numbers.

In the above example the answer is: [1 (1st in row 1), 5 (2nd in row 2), 2 (2nd in row 3), 3 (2nd in row 4)]

Implement a method that gets the above structure in a 2-D array (zero padded), and returns the list with the highest sum.


The above example will be passed to this method like below:
[
    [1, 0, 0, 0]
    [9, 5, 0, 0]
    [3, 2, 1, 0]
    [1, 3, 2, 1]
]

List<Integer> highestSumList(List<List<Integer>> lst) {...}
=============================================================================


Question 5
==========

write a number as sum of prime numbers, As there are multiple answers for each number. Answer we are looking for should consist of non-repeating primes.

e.g. 9 = 2+2+2+3 OR 7+2 (7+2 is the CORRECT answer)
      6 = NO SOLUTION based on the restrictions
      5 = 3+2


List<Integer> sumOfPrimes(Int number){}
