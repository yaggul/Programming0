n=0
while str(n)=='' or int(n)<100 or int(n)>999:
    n=input("\nPlease enter a number between 100 and 999: ")
n=int(n)
a=n%10
n=n//10
b=n%10
n=n//10
c=n%10
ub=''
lb=''
if a>b and a>c:
    if b>c:
        ub+=str(a)+str(b)+str(c)
        lb+=str(c)+str(b)+str(a)
    elif c>b:
        ub+=str(a)+str(c)+str(b)
        lb+=str(b)+str(c)+str(a)
    elif c==b:
        ub+=str(a)+str(b)+str(c)
        lb+=str(b)+str(c)+str(a)
elif b>a and b>c:
    if a>c:
        ub+=str(b)+str(a)+str(c)
        lb+=str(c)+str(a)+str(b)
    elif c>a:
        ub+=str(b)+str(c)+str(a)
        lb+=str(a)+str(c)+str(b)
    elif c==a:
        ub+=str(b)+str(a)+str(c)
        lb+=str(a)+str(c)+str(b)
elif c>a and c>b:
    if a>b:
        ub+=str(c)+str(a)+str(b)
        lb+=str(b)+str(a)+str(c)
    elif b>a:
        ub+=str(c)+str(b)+str(a)
        lb+=str(a)+str(b)+str(c)
    elif a==b:
        ub+=str(c)+str(a)+str(b)
        lb+=str(a)+str(b)+str(c)
elif a==b and a==c:
    ub+=str(a)+str(b)+str(c)
    lb+=str(a)+str(b)+str(c)
elif a==c and b<c:
    ub+=str(a)+str(c)+str(b)
    lb+=str(b)+str(a)+str(c)
elif b==c and a <b:
    ub+=str(b)+str(c)+str(a)
    lb+=str(a)+str(b)+str(c)
#print("The largest number is {}".format(ub))
#print("The smallest number is {}".format(lb))
print("The largest number is ",end=''),print(int(ub))
print("The smallest number is ",end=''),print(int(lb))
