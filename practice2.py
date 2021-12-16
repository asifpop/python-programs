class gad:
	def cal(self,x,y):
		return x*y
		
item=gad()
item.price=500
item.q=5
print(item.cal(item.price,item.q))