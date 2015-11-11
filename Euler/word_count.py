#!/usr/bin/env python

from __future__ import print_function


some_string = "I am that I am that I am that I was and will be"

def word_count(some_string):
	some_dict = {}

	for word in some_string.split():
		print(word)
		if word in some_dict:
			some_dict[word] = some_dict[word] + 1
		else:
			some_dict[word] = 1

		
	return some_dict

print(word_count(some_string))