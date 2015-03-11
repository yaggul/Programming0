def is_prime(n):
    m=n-1
    while m>1:
        if n%m==0:
            return False
        m-=1
    return True


def prime_pair(items):
    cnum=0
    nums=[]
    for i in range(len(items)):
        for j in range(i,len(items)):
            check=items[i]+items[j]
            if is_prime(check)==True:
                return True
            else:
                pass
    return False



def main():
    if __name__=='__main__':
        main()
