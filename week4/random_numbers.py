def generate_random_list(n,start,end):
    from random import randint
    count=0
    lst=[]
    while count<n:
        lst+=[randint(start,end)]
        count+=1
    return lst
