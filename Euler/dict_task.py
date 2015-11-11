#!/usr/bin/env python

from __future__ import print_function

dicts = [
	{'name':'Mick',
	 'food':'PIZZA'},
	{'name':'Garfield',
	 'food':'lasanga'},
	{'name':'Walter',
	 'food':'pancakes'},
	{'name': 'Galactus',
	 'food': 'worlds'}
]

stringy = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(some_dict, some_string):
	sentence_list=[]
	for key in some_dict:
		new_string = some_string.format(**key)
		sentence_list.append(new_string)
	return sentence_list

print(string_factory(dicts,stringy))
