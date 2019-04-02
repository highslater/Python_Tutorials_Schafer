#!/usr/bin/env python3.7

"""007_Loops_and_Iterations.py.

Seventh Program of the Corey Schafer Python Series.

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
logging.basicConfig(filename="LOG_files/LOG_007.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("007_Loops_and_Iterations.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

nums = [1, 2, 3, 4, 5]

print('', "-" * 88)
for num in nums:
    print('', num)
print('', "-" * 88)

print('', "-" * 88)
for num in nums:
    if num == 3:
        print('', 'Found It.')
        break
    print('', num)
print('', "-" * 88)

print('', "-" * 88)
for num in nums:
    if num == 3:
        print('', 'Found It.')
        continue
    print('', num)
print('', "-" * 88)

print('', "-" * 88)
for num in nums:
    for letter in "abc":
        print('', num, letter)
print('', "-" * 88)

print('', "-" * 88)
for i in range(1, 11):
    print('', i)
print('', "-" * 88)

print('', "-" * 88)
x = 0
while x < 10:
    print('', x)
    x += 1
print('', "-" * 88)

print('', "-" * 88)
x = 0
while x < 10:
    if x == 5:
        break
    print('', x)
    x += 1
print('', "-" * 88)

print('', "-" * 88)
x = 0
while True:
    if x == 5:
        break
    print('', x)
    x += 1
print('', "-" * 88)
