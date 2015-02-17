n=int(input("Please insert a number: "))
primes=[]
noprimes=[]
for i in str(n):
	m=int(i)-1
	while m>1:
		if int(i)%m==0:
			noprimes+=[m]
		m-=1
	if len(noprimes)==0:
		primes+=[i]
print(primes)
if len(primes)>0:
	print('True')
else:
	print('False')