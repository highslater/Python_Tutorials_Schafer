#!/usr/bin/env python3.7

"""004_Lists_Sets_and_Tuples.py.

Fourth Program of the Corey Schafer Python Series.

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
logging.basicConfig(filename="LOG_files/LOG_004.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("004_Lists_Sets_and_Tuples.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

courses = ['History', 'Math', 'Physics', 'CompSci']
courses2 = ['Art', 'Education']

print(courses[:2])
print(courses[2:])

courses.append('Art')

print(courses)

courses.insert(0, 'Art')
print(courses)

courses.insert(0, courses2)
print(courses)

courses.extend(courses2)
print(courses)

courses.remove('Math')
print(courses)

courses.remove('Art')
print(courses)

courses.remove('Art')
print(courses)

courses.remove(courses2)
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
courses.reverse()
print(courses)

courses.sort()
print(courses)

nums = [1, 5, 2, 4, 3]
print(nums)
nums.sort()
print(nums)

courses.sort(reverse=True)
print(courses)
nums.sort(reverse=True)
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(nums)
print(sorted(nums))
print(nums)

print(courses)
print(sorted(courses))
print(courses)

print(nums)
print((min(nums), max(nums), sum(nums)))
print("Min: {}, Max: {}, Sum: {}".format(min(nums), max(nums), sum(nums)))
print(f"Min: {min(nums)}, Max: {max(nums)}, Sum: {sum(nums)}")
print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
nums = [1, 5, 2, 4, 3]

print(courses.index('CompSci'))
print('CompSci index: {}'.format(courses.index('CompSci')))
print(f"CompSci index: {courses.index('CompSci')}")

print(f"Is 'Art' in courses?: {'Art' in courses}")
print(f"Is 'Math' in courses?: {'Math' in courses}")

for item in courses:
    print(item, end=", ")
print()

for index, course in enumerate(courses, start=1):
    print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)

tpl = ([1, 2], [3, 4])

print(tpl)

tpl[0][0] = 0
tpl[0][1] = 0
tpl[1][0] = 0
tpl[1][1] = 0

print(tpl)

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)
print('Math' in cs_courses)

print(cs_courses)
print(art_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
