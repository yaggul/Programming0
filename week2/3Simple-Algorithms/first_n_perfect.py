n=int(input("Enter count: "))
pnumbers=[]
num=2
m=num
count=1
collectorD=0
divisors=[]
while len(pnumbers)<n:
	while count<num:
		m-=1
		if num%m==0:
			collectorD+=m
			divisors+=[m]
		else:
			pass
		count+=1
	if collectorD==num:
		pnumbers+=[collectorD]
	else:
		pass
	num+=1
	m=num
	count=1
	collectorD=0
for i in pnumbers:
	print(i)