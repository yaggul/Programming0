def twinp(n):
	from is_prime import is_prime
	test=[n-2,n,n+2]
	twins=[]
	if is_prime(n)==False:
		return "{} is not a prime.".format(n)
	else:
		#print("{} is prime but:".format(n))
		for i in [test[0],test[2]]:
			if is_prime(i)==True:
				twins+=[i]
			else:
				pass
		if len(twins)==0:
			print("{} is prime but:\n{} is not.\n{} is not.".format(n,test[0],test[2]))
		else:
			print("Twin primes with {}:".format(n))
			for i in twins:
				print("{}, {}".format(n,i))
def main():
	if __name__=='__main__':
		main()
