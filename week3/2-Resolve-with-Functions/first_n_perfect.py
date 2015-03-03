def first_n_perfect(n):
	from is_perfect import is_perfect
	pnumbers=[]
	num=2
	while len(pnumbers)<n:
		if is_perfect(num)==True:
			pnumbers+=[num]
		else:
			pass
		num+=1
	return pnumbers

def main():
	if __name__=='__main__':
		main()
