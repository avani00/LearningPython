a = 1
b = 1

while True:
	try:
		n = int(input("How many numbers do you want? "))
	except: 
		print('Not Valid')
	else:
		break

if n > 0:
	print(a)
	if n > 1:
		print(b)

count = n - 2

while count > 0:
	c = a + b
	a = b
	b = c
	print(c)
	count -= 1