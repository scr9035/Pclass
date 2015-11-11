from __future__ import print_function
import math


numbers = raw_input('Enter two numbers, flips and num coins: ')
numbers = numbers.split()


def combo(n, m):
	"""given 2 integers finds N heads on M coin flips"""

	if n == 0:
		return 1
	else:
		answ = math.factorial(n)/(math.factorial(m)*math.factorial(n-m))
		return answ


print(combo(int(numbers[0]),int(numbers[1])))
