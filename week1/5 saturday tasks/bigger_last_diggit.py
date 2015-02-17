n=int(input("\nPlease insert first number: "))
m=int(input("\nPlease insert second number: "))
if (n%10)==(m%10):
    if n>m:
        print(n)
    elif m>n:
        print(m)
    else:
        print("n({}) and m({}) are equal!".format(n,m))
elif (n%10)>(m%10):
    print(n)
else:
    print(m)