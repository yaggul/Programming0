n=int(input("Enter count of numbers: "))
count=1
numbers=[]
while count<=n:
	number=int(input("Please enter a number: "))
	numbers=numbers+[number]
	count+=1
numbers.sort()
print(numbers[-1])