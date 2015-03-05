def reverse_int(n):
	n_ls=[]
	while n>0:
		n_ls+=[n%10]
		n=n//10
	for i in n_ls:
		n=n*10+i
	return n

def sum_digits(n):
	n_ls=[]
	while n>0:
		n_ls+=[n%10]
		n=n//10
	for i in n_ls:
		n+=i
	return n

def product_digits(n):
	n_ls=[]
	while n>0:
		n_ls+=[n%10]
		n=n//10
	n=1
	for i in n_ls:
		n*=i
	return n

def main():
	if __name__=='__main__':
		main()
