class gadget:
	def __init__(self, price,quantity):
		self.priceofgadgets=price
		self.quantityofgadgets=quantity
	def calculate(self):
		return self.priceofgadgets*self.quantityofgadgets

item1=gadget(200,5)
item2=gadget(400,5)

print(item1.calculate())
print(item2.calculate())