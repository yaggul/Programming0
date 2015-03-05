def is_triangle(a,b,c):
    if max(a,b,c)-min(a,b,c)<(a+b+c)-(max(a,b,c)+min(a,b,c)) and max(a,b,c)+min(a,b,c)>(a+b+c)-(max(a,b,c)+min(a,b,c)):
        return True
    else:
        return False


#S=sqrtp(p-a)(p-b)(p-c)

def area(a,b,c):
    p=(a+b+c)/2
    s=round((p*(p-a)*(p-b)*(p-c))**0.5,2)
    return s

def is_pythagorean(a,b,c):
    '''
    За да бъде елиминиран човешкият фактор 
    функцията сама намира коя страна е вероятната хипотенуза,
    след което проверява за питагоровото равенство :-)))
    '''
    h=[]
    k=[]
    for i in (a,b,c):
        if i==max(a,b,c):
            h+=[i]
        else:
            k+=[i]
    if h[0]**2==k[0]**2+k[1]**2:
        return True
    else:
        return False
    
def max_area(triangles):
    arealst=[]
    for i in triangles:
        arealst+=[area(i[0],i[1],i[2])]
    for j in triangles:
        if area(j[0],j[1],j[2])==max(arealst):
            return j
        else:
            pass





def main():
    if __name__=='__main__':
        main()
        
