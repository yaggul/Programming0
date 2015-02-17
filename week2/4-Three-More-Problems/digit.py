n=int(input("Please insert a number to convert: "))
digits=[]
while n>0:
	digits=[n%10]+digits
	n=n//10
print("The list of digits is {}".format(digits))
start=0
while start<=len(digits)-1:
	n=n*10+digits[start]
	start+=1
print("The number is {}.".format(n))