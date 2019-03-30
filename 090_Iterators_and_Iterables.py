#!/usr/bin/env python3.7

"""090_Iterators_and_Iterables.py.

Ninteieth Program of the Corey Schafer Python Series.

"""
import logging
import os
from platform import python_version
from sys import hexversion
from datetime import datetime as dt

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_090.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("090_Iterators_and_Iterables.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


nums = [1, 2, 3]

for num in nums:
    print(num, end=", ")
else:
    print("\n")

[print(num, end=", ") for num in nums]
print()

'''
print(dir(nums))

... '__iter__',... is iterable but no __next__ so is not an iterator

'''

'''
i_nums = nums.__iter__()
or
i_nums = iter(nums)

print(i_nums)
print(dir(i_nums))

<list_iterator object at 0x7f1e4e208f28>

['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__',
'__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__',
'__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']


'''

# i_nums = iter(nums)
# for i in range(len(nums) + 1):
#     print(next(i_nums))

# 1
# 2
# 3
# Traceback (most recent call last):
#   File "./090_Iterators_and_Iterables.py", line 72, in <module>
#     print(next(i_nums))
# StopIteration

i_nums = iter(nums)

for i in range(len(nums) + 1):
    try:
        print(next(i_nums))
    except StopIteration:
        print("hit except StopIteration:")
        break


class MyRange():
    """Docstring for MyRange."""

    def __init__(self, start, end):
        """Docstring for __init__."""
        self.value = start
        self.end = end

    def __iter__(self):
        """Docstring for __iter__."""
        return self

    def __next__(self):
        """Docstring for __next__."""
        if self.value >= self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value

nums = MyRange(1, 10)

for i in MyRange(1, 11):
    try:
        print(next(nums))
    except StopIteration:
        print("hit except StopIteration:")
        break


def my_range(start, end):
    """Docstring."""
    current = start
    while current < end:
        yield current
        current += 1

nums = my_range(1, 10)

for i in my_range(1, 11):
    try:
        print(next(nums))
    except StopIteration:
        print("hit except StopIteration:")
        break
