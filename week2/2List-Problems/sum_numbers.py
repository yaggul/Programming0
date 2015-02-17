n=int(input("Please insert how many numbers will be inserted: "))
count=1
numbers=[]
while count<=n:
	number=int(input("Enter a number: "))
	numbers=numbers+[number]
	count+=1
collector=0
for i in numbers:
	collector+=i
print("The sum is {}".format(collector))