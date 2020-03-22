#quantity = 15
#price = 11.290

itemComp = open('itemList.txt','r')
def itemCalculator(quantity,price):
	total = quantity*price
	print("Your total is: "+str(total))

class items:
	def __init__(self,itemName,price):
		itemName = str(self.itemName)
		price = self.price




quant = float(input("Enter quantity: "))
priceE = float(input("Enter price: "))

itemCalculator(quant,priceE)
