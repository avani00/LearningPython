'''
shows the tax
'''

def taxamount(cost, tax):
	totalcost = (cost * tax * 0.01) + cost
	return totalcost

money = int(input("How much money is the tax being put on? "))
tax = int(input("How much is the tax? "))
totaltaxcost = taxamount(money, tax)
print(totaltaxcost)