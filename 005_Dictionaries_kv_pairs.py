#!/usr/bin/env python3.7

"""005_Dictionaries_kv_pairs.py.

Fifth Program of the Corey Schafer Python Series.

"""
import logging
import os
from platform import python_version
from sys import hexversion
from datetime import datetime as dt
import random

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

NOW = dt.today()
PRINT_VERSION_INFO = True
PRINT_TIME = True
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
version_info = "The Python Version is: {}  #{}".format(
    python_version(), str(hexversion))
logging.basicConfig(filename="LOG_files/LOG_005.Log",
                    level=logging.DEBUG, format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()
logger.info(version_info) if PRINT_VERSION_INFO else None
logger.info(NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
logger.info("005_Dictionaries_kv_pairs.py RUN / START")

print("Today is:", NOW.strftime("%A, %B, %d, %Y")) if PRINT_TIME else None
print(version_info) if PRINT_VERSION_INFO else None


def make_encryption_dicts():
    """Docstring."""
    # ??or zip with random choice from range(1,27) ??
    decrypt = "abcdefghijklmnopqrstuvwxyz"
    decrypt = list(decrypt)
    random.shuffle(decrypt)
    decrypt = dict(enumerate(decrypt, start=1))
    encrypt = {}
    for k, v in decrypt.items():
        encrypt.update({v: k})
    return decrypt, encrypt


def cipher(plain_text, e):
    """Docstring."""
    cipher_text, i = "", 0
    for p in plain_text:
        cipher_text += str(e[p]) if i == 0 else "-" + str(e[p])
        i += 1
    return cipher_text


def de_cipher(cipher_text, d):
    """Docstring."""
    plain_text, p = [], list(cipher_text.split("-"))
    for c in p:
        plain_text.append(d[int(c)])
    return ("".join(plain_text))

#
# message = 'secrets'
# d, e = make_encryption_dicts()
# c_text = cipher(message, e)
# print(c_text)
# p_text = de_cipher(c_text, d)
# print(p_text)


student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

print(student.get('name', 'Not Found'))
print(student.get('phone', 'Not Found'))

student['phone'] = '555-1212'
print(student.get('phone', 'Not Found'))

student['name'] = 'Jane'
print(student.get('name', 'Not Found'))

student.update({'name': "Jane", 'age': 26, 'phone': '555-5555'})
print(student)

del student['age']
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
age = student.pop('age')
print(age)
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for s in student:
    print(s)

for key, value in student.items():
    print(key, value)
