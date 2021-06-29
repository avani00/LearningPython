'''
reverses the string
'''

def reversestring(stringinput):
	reversever = stringinput[::-1]
	return reversever

stringinput = input("You're string here: ")
reversedstring = reversestring(stringinput)

print(reversedstring) 