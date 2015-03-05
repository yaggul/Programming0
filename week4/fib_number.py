def fib_number(n):
    a=0
    b=1
    count=0
    fibs=[]
    while count<n:
        fibs+=[b]
        a,b=b,a+b
        count+=1
    digits=[]
    for i in fibs:
        mid=[]
        while i>0:
            mid=[i%10]+mid
            i=i//10
        digits=digits+mid
    num=0
    for i in digits:
        num=num*10+i
    return fibs,num

def main():
    if __name__=='__main__':
        main()
