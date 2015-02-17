n=int(input("\nPlease enter a number: "))
m=n
collector=''
while m>0:
    collector+=str(m%10)
    m=m//10
if n==int(collector):
    print("The number {} is palindrom.".format(n))
else:
    print("The number {} is not palindrom.".format(n))