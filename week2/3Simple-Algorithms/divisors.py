n=int(input("Please insert a number: "))
divisors=[]
count=1
m=n
while count<n:
	m-=1
	if n%m==0:
		divisors+=[m]
	#m-=1
	count+=1
print("The devisors of {} are {}.".format(n,divisors))