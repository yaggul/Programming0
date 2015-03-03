def to_digit(n):
	digits=[]
	while n>0:
		digits=[(n%10)]+digits
		n=n//10
	return digits


def is_prime(n):
	m=n-1
	while m>1:
		if n%m==0:
			return False
		m-=1
	return True

def main():
	if __name__=="__main__":
		main()
