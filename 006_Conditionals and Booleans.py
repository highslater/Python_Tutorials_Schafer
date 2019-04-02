#!/usr/bin/env python3.7

"""006_Conditionals and Booleans.py.

Fifth Program of the Corey Schafer Python Series.

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
logging.basicConfig(filename="LOG_files/LOG_006.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("006_Conditionals and Booleans.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None

if True:
    print('Condition was True.')

language = 'Python'
if language == 'Python':
    print('The language is Python.')
else:
    print('No match.')

language = 'Java'
if language == 'Python':
    print('The language is Python.')
else:
    print('No match.')

language = 'Java'

if language == 'Python':
    print('The language is Python.')
elif language == 'Java':
    print('The language is Java')
else:
    print('No match.')

language = 'JavaScript'

if language == 'Python':
    print('The language is Python.')
elif language == 'Java':
    print('The language is Java')
elif language == 'JavaScript':
    print('The language is JavaScript')
else:
    print('No match.')

user, logged_in = 'Admin', True
print('Admin Page' if user == 'Admin' and logged_in else 'Bad Creds')

user, logged_in = 'Admin', False
print('Admin Page' if user == 'Admin' and logged_in else 'Bad Creds')

user, logged_in = 'Admin', False
print('Admin Page' if user == 'Admin' or logged_in else 'Bad Creds')

user, logged_in = 'User', True
print('User Page' if user == 'Admin' or logged_in else 'Bad Creds')

user, logged_in = 'User', True
print('Please log in' if not logged_in else f'Welcome {user}')

user, logged_in = 'User', False
print('Please log in' if not logged_in else f'Welcome {user}')

a, b = [1, 2, 3], [1, 2, 3]
c = a
print(id(a), id(b), id(c))

print("-" * 88)
print('a == b: ', a == b)
print(f'a == b because {a} is the same list as {b}. Even though their id\'s'
      f' {id(a)}, {id(b)} are different.')
print(f'id(a) == id(b): {id(a) == id(b)}')

print("-" * 88)
print('a is b: ', a is b)
print(f'Even though {a} and {b} are the same, list_a is not list_b'
      f' because list_a\'s id {id(a)} is not the same as list_b\'s {id(b)}')
print(f'id(a) == id(b): {id(a) == id(b)}')

print("-" * 88)
print('a is c: ', a is c)
print(f'list_c, ({c}) is a copy of list_a, ({a}). So their id\'s'
      f' {id(c)}, {id(a)} are the same.')
print(f'id(a) == id(c): {id(a) == id(c)}')

print('', "-" * 88)
conditions = [False, None, 0, '', (), [], {}]
for condition in conditions:
    if condition == '':
        print('', "''\t:", bool(condition))
    else:
        print('', condition, "\t:", bool(condition))
print('', "-" * 88)


print('', "-" * 88)
conditions = [False, None, 0, '', (), [], {}]
for condition in conditions:
    print('', condition if condition != '' else "''", "\t:", bool(condition))
print('', "-" * 88)
