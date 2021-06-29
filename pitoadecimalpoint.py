pi = '3.14159265358979323846264338327950288419716939937510'

n = int(input('What digit do you want to find pi to? '))

while n > 50:
	print('Not Valid')
	n = int(input('What digit do you want to find pi to? '))

n += 2
print(pi[:n])