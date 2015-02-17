print("Welcome to Calculator")
print()
oper=['+','-','*','/',]
a=int(input("Please enter first number: "))
b=int(input("Please enter second number: "))
oPer=str(input("Please choose from the following operations {}: ".format(oper)))
print()
if oPer=='+':
    print(int(a+b))
elif oPer=='-':
    print(int(a-b))
elif oPer=='*':
    print(int(a*b))
elif oPer=='/':
    print(float(a/b))
elif oPer not in oper:
    print("We do not support that operation")