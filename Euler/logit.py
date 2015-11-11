from __future__ import print_function
import math

coeff = [2,3,4,-1,2,.5]


def logit(coeff):

	Bo = float(coeff[-1])
	B = float(coeff[-2])
	x = float(coeff[-3])

	demon = math.e**(-(Bo + B*x))
	logit_value = 1/(1+demon)
	print(logit_value)

logit(coeff)