def prime_digit(n):
	from is_prime import is_prime,to_digit
	for i in to_digit(n):
		if is_prime(i)==True:
			return True
		else:
			pass
	return False	
	
def main():
	if __name__=='__main__':
		main()
