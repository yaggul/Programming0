def to_digit(n):
	digits=[]
	while n>0:
		digits=[(n%10)]+digits
		n=n//10
	return digits


def to_number(n):
	num=0
	for i in n:
		num=num*10+i
	return num

def max_number(y):
	return sorted(y,reverse=True)

def min_number(m):
	return sorted(m)


n=int(input("Please insert a number with more than one digit: "))
print("Largest: {}".format(to_number(max_number(to_digit(n)))))
print("Smallest: {}".format(to_number(min_number(to_digit(n)))))
