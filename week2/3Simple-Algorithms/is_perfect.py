n=int(input("Please insert a number: "))
count=1
m=n
divisors=[]
collectD=0
while count<n:
	m-=1
	if n%m==0:
		divisors+=[m]
		collectD+=m
	count+=1
if collectD==n:
	print("This number n({}) is perfect: ".format(n))
else:
	print("This number n({}) is not perfect.".format(n))