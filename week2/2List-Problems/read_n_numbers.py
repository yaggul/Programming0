n=int(input("Enter count of numbers to input: "))

count=1
numbers=[]

while count<=n:
	number=int(input("Enter a number: "))
	
	numbers=numbers+[number]
	count+=1
print(numbers)