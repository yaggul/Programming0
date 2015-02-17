p=int(input("Please insert a number: "))
primes=[]
nonprimes=[]
test=[p-2,p,p+2]
for i in test:
	m=i-1
	while m>1:
		if i%m!=0:
			m-=1
		else:
			nonprimes+=[i]
			break
	if i not in nonprimes:
		primes+=[i]
	else:
		pass
if p in nonprimes:
	print("{} is not a prime.".format(p))
else:
	if test[0] in nonprimes and  test[2] in nonprimes:
		print("{} is prime but:".format(test[1]))
		print("{} and {} are not primes.".format(test[0],test[2]))	
	elif test[0] in nonprimes:
		print("Twin primes with {}:".format(p))
		print("{}".format(test[2]))
		print("But {} is not a prime.".format(test[0]))
	elif test[2] in nonprimes:
		print("Twin primes with {}:".format(p))
		print("{}".format(test[0]))
		print("But {} is not a prime.".format(test[2]))
	else:
		print("Twin primes with {}:".format(p))
		print("{}, {}".format(test[0],test[1]))
		print("{}, {}".format(test[1],test[2]))