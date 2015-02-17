n=int(input("Please insert a number: "))
def fact(n):
	if n==0:
		return 1
	else:
		factoriel=1
		start=1
		while start<=n:
			factoriel=factoriel*start
			start+=1
		return factoriel
print("fact({}) == {}".format(n,fact(n)))