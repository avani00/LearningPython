'''
Prime Factorization
'''

number = int(input("What number do you want the prime factorization of? "))
primes = []

for num in range (2, number//2 + 1):
	while number%num == 0:
		primes.append(num)
		number = number/num

print(primes)