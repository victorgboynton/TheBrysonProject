#quantity = 15
#price = 11.2



class items:
	def __init__(self,itemName,price):
		itemName = str(self.itemName)
		price = self.price

itemCatalog = [] 

with open("itemList.txt") as f:
	x=1
	for line in f:
		itemCatalog[x] = line
		x = x + 1




def itemCalculator(quantity,price):
	total = quantity*price
	print("Your total is: "+str(total))

	


quant = float(input("Enter quantity: "))
priceE = float(input("Enter price: "))

itemCalculator(quant,priceE)
