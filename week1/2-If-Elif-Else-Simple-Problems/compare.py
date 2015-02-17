print()
print("Welcome to compare tool")
print()
a=int(input("Please insert first number 'a': "))
b=int(input("Please insert second number 'b': "))
if a==b:
    print('a({}) is equal to b({})!'.format(a,b))
elif a>b:
    print('a({}) is bigger than b({})!'.format(a,b))
else:
    print('b({}) is bigger than a({})!'.format(b,a))