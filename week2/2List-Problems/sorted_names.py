n=int(input("Please insert number of names: "))
count=1
names=[]
while count<=n:
	name=input("Please insert a name: ")
	names=names+[name]
	count+=1
names=sorted(names)
print("Sorted names are: ")
for name in names:
	print(name)