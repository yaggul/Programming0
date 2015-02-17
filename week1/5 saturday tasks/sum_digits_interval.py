N=int(input("Please insert the first number: "))
M=int(input("Please insert the second number: "))
collector=0
n=0
if N==M:
    n=N
    while n>0:
        collector+=n%10
        n=n//10
    print("N({}) and M({}) are equal!".format(N,M))
    print("Sum of digits of {} is {}".format(N,collector))
elif N>M:
    n=M
    while M<=N:
        n=M
        collector=0
        while n>0:
            collector+=n%10
            #print("Collector = {}".format(collector))
            n=n//10
            #print("n = {}".format(n))
        print("Sum of digits of {} = {}".format(M,collector))
        M+=1
elif M>N:
    n=N
    while N<=M:
        n=N
        collector=0
        while n>0:
            collector+=n%10
            n=n//10
        print("Sum of digits of {} = {}".format(N,collector))
        N+=1