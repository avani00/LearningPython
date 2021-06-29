'''
returns change
'''

cost = float(input("What is the cost of the items? "))
given = float(input("How much money did you give? "))

change = round(given - cost, 2)
changeamount = change
change = int(change * 100)

quarters = 0
dimes = 0
nickels = 0
pennies = 0

while change >= 25:
	change -= 25
	quarters += 1
while change >= 10:
	change -= 10
	dimes += 1
while change >= 5:
	change -= 5
	nickels += 1
while change > 0:
	change -= 1
	pennies += 1

print("Change: " + str(changeamount))
print("Quarters: " + str(quarters) + " " + "Dimes: " + str(dimes) + " " + "Nickels: " + str(nickels) + " " + "Pennies: " + str(pennies))
