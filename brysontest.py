#quantity = 15
#price = 11.2



class items:
	def __init__(self,itemName,price):
		itemName = str(self.itemName)
		price = self.price

itemCatalog = [] 

with open("itemList.txt") as f:
	for line in f:
		line = line.replace("\n","")
		itemCatalog.append(line.split(','))


itemClassCatalog = []
for x in range(0,len(itemCatalog)):
	for y in range(1,2):
		itemClassCatalog.append(itemCatalog[x][y])




def itemCalculator(quantity,price):
	total = quantity*price
	print("Your total is: "+str(total))

	


quant = float(input("Enter quantity: "))
priceE = float(input("Enter price: "))

itemCalculator(quant,priceE)
