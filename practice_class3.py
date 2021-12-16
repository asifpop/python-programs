class gad:
	def __init__(self, name :str, price:int, quantity=0):
		
		assert price>=0, f"price {price} should be greater than or equal to zero"
		assert quantity>=0, f"quantity {quantity} should be greater than or equal to zero"
		
		self.n=name
		self.p=price
		self.q=quantity
	def cal(self):
		return self.p*self.q
		
item=gad("phone",8,-6)
print(item.n)
print(item.cal())
