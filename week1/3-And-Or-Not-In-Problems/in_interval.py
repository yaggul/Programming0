print()
print("Welcome to is it in the interval!!!")
print()
lb=int(input("Please insert the lower bound of the interval: "))
ub=int(input("Please insert the upper bound of the interval: "))
num=int(input("Please insert a number to check: "))
if lb==ub and lb==num:
    print()
    print("{},{} and {} are all equal".format(lb,ub,num))
    print()
elif num==lb:
    print()
    print("The number is equal to the lower bound of the interval!")
    print()
elif num==ub:
    print()
    print("The number is equal to the upper bound of the interval!")
    print()
elif lb<num and num<ub:
    print()
    print("The number is in the interval {}-{}".format(lb,ub))
    print()
elif num<lb:
    print()
    print("The number is outside the interval {} < {}".format(num,lb))
    print()
else:# num>ub:
    print()
    print("The umber is outside the interval, {} > {}".format(num,ub))
    print()

    
