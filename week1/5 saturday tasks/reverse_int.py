n=int(input("\nPlease enter a number: "))
m=n
collector=''
while n>0:
    collector+=str(n%10)
    n=n//10
print("\nThe reverse int of {} without leading zero is :".format(m),end=' '),print(int(collector))