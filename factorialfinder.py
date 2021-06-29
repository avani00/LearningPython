'''
finds the factorial of a number
'''

def factorial(n):
	number = n 
	total = 1
	for num in range(0,n - 1):
		total = total * number
		number -= 1
	return total

numb = int(input("What number do you want the factorial of? "))
print(factorial(numb))