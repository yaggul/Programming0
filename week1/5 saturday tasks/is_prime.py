n=int(input("\nEnter a number: "))
m=n-1
while m>1:
    if n%m==0:
        print("n({}) is not prime".format(n))
        quit()
    m-=1
print("n({}) is prime)".format(n))