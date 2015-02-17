n=int(input("\nplease insert a number: "))
collector=0
while n>0:
    collector+=(n%10)
    n=n//10
print("sum is {}".format(collector))
