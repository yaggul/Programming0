def gen_orders():
    count=0
    beers=[]
    fries=[]
    n=int(input("Please insert number of orders of beers and fries: "))
    while count<n:
        beers+=[int(input("Please insert your score for every beer order: "))]
        count+=1
    count=0
    while count<n:
        fries+=[int(input("Please insert you score for every fries order: "))]
        count+=1
    return sorted(beers),sorted(fries)


def max_score(beers,fries):
    total_score=0
    i=0
    j=0
    while i<len(beers):
        while j<len(fries):
            total_score+=(beers[i]*fries[j])
            i+=1
            j+=1
    return total_score
beers,fries=(gen_orders())
print(max_score(beers,fries))
