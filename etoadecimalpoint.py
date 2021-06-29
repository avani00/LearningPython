e = '2.7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'

n = int(input('What digit do you want to find e to? '))

while n > 100:
	print('Not Valid')
	n = int(input('What digit do you want to find e to? '))

n += 2
print(e[:n])