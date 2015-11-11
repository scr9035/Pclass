from __future__ import print_function
import math


#numbers = raw_input('Enter two numbers, flips and num coins: ')
for line in sys.stdin:
	numbers = line

numbers = numbers.split()

collatz_num = int(numbers[0])

for i in range(int(numbers[1])):
	if collatz_num % 2 == 0:
		collatz_num = collatz_num / 2
	else:
		collatz_num = 3*collatz_num+1
	

print(collatz_num)