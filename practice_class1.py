class gadget:
	def calculate(self,x,y):
		return x*y
item1=gadget()
item1.price=100
item1.quantity=3
print(item1.calculate(item1.price,item1.quantity))

item2=gadget()
item2.price=400
item2.quantity=5
print(item2.calculate(item2.price,item2.quantity))