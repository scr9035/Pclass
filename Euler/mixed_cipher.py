#!/usr/bin/env python
"""Scott Riggs scr9035
This program asks the user to input a secret cypher
and then uses their cypher to scramble a message
from an input text file"""

#Makes print a function as is standard in python 3
from __future__ import print_function
import string
import sys
from string import maketrans


def remove_duplicates(string2):
    """removes any duplicate letters of an input string"""
    result = []
    seen = set()
    for char in string2:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

#Open secret file
with open(sys.argv[1], 'r') as CODE:
    SECRET_FILE = CODE.read()

#prompt user for their secret code
MIXED_CI = raw_input("Please enter a keyword for the mixed cypher: ")

#cipher input to lowercase, removes all numbers and punctuation
MIXED_CI = MIXED_CI.lower().replace(" ", "").translate(None, string.digits)
MIXED_CI = MIXED_CI.translate(None, string.punctuation)

#removes duplicate letters
MIXED_CI = remove_duplicates(MIXED_CI)

#turns the lowercase ascii to the cipher code
LOWER_ASCII = string.ascii_lowercase.translate(None, MIXED_CI)
CIPHER_CODE = MIXED_CI + LOWER_ASCII

#makes lower and upper case substitution tables
TRANS_TABLE_LOWER = maketrans(string.lowercase, CIPHER_CODE)
TRANS_TABLE_UPPER = maketrans(string.uppercase, CIPHER_CODE.upper())

#outputs the starting alphabet, cipher code, and secret code
print("Plaintext: " + string.lowercase)
print("Ciphertext: " + CIPHER_CODE)
print(SECRET_FILE.translate(TRANS_TABLE_LOWER).translate(TRANS_TABLE_UPPER))



