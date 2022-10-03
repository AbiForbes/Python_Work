from operator import floordiv, mod

def sum_of_factoral_digits(x):
	"""The sum of the digits in the number 10! is 27.
	   Find the sum of the digits in the number 100!
	
	>>> sum_of_factoral_digits(10)
	27
	"""

	sum_of_factorial_digits = sum_of_digits(factorial(x))
	print( sum_of_factorial_digits)

def factorial(n):
	factorial_of_n = 1
	for i in range(1, n):
		factorial_of_n = factorial_of_n * i
	return factorial_of_n
		
def sum_of_digits(n):
	string_n = str(n)
	length_of_n = len(string_n)
	n_reduced = n
	sum_of_digits = 0
	for i in range (0, length_of_n):
		sum_of_digits = sum_of_digits + mod(n_reduced, 10)
		n_reduced= floordiv(n_reduced, 10)
	return sum_of_digits

sum_of_factoral_digits(100)
