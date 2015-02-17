n=int(input("Please insert how many numbers will be entered: "))
count=1
numbers=[]
evens=[]
while count<=n:
	number=int(input("PLease insert a number: "))
	numbers=numbers+[number]
	count+=1
for i in numbers:
	if i%2==0:
		evens=evens+[i]
print("Count of evens: {}".format(len(evens)))
print("Evens are:")
for i in evens:
	print(i)