n=int(input("Please insert th number of elements: "))
start=0
items=[]
while start<n:
	elem=input("Please insert an element: ")
	items+=[elem]
	start+=1
	
def countEL(items):
	counter=0
	for i in items:
		counter+=1
	return counter
print("count_elements({}) == {}".format(items,countEL(items)))