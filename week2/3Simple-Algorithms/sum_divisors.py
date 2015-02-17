n=int(input("Please insert a number: "))
count=1
m=n
collector=0
while count<n:
	m-=1
	if n%m==0:
		collector+=m
	count+=1
print("The sum of devisors is {}.".format(collector))