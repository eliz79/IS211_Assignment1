#! usr/bin/env python
# *-* coding: utf-8 *-*
"""Week 1 IS 211 Assignment - Part 1"""


class ListDivideException(Exception):
    """A custom exceptions class."""
    def __init__(self, msg):
        self.msg = msg


def listDivide(numbers, divide=2):
    """To be able to return a number of elements.
    Args:
        numbers(list): a list of numbers
        divide(integer): a divisor integer

    Return:
        The number of elements in the numbers list that are divisible by divide.
    Example:
        >>> listDivide([1,2,3,4,5,6])
        3
        >>> listDivide([2,4,6,8,10])
        5
    """
    mylist = []
    for i in numbers:
        if i % divide == 0:
            mylist.append(i)
    return len(mylist)


def testListDivide():
    """Test for listDivide function."""

    tests = [
        ([1, 2, 3, 4, 5]),
        ([2, 4, 6, 8, 10]),
        ([30, 54, 63, 98, 100]),
        ([]),
        ([1, 2, 3, 4, 5])
        ]
    for i in tests:
        if listDivide != divide:
            raise ListDivideException('Test Failed')
