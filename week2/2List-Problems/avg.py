n=int(input("Please enter how many numbers will be inserted: "))
count=1
numbers=[]
collector=0
counter=0
while count<=n:
	number=int(input("Please enter a number: "))
	numbers=numbers+[number]
	count+=1
for i in numbers:
	collector+=i
	counter+=1
print("Avg is {}".format(collector/counter))