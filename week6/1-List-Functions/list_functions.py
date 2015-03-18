#head
def head(items):
    if items==[]:
        return []
    else:
        return items[0]

#last
def last(items):
    if items==[]:
        return []
    else:
        return items[len(items)-1]

#tail
def tail(items):
    if items==[]:
        return []
    else:
        res=[]
        for i in range(1,len(items)):
            res+=[items[i]]
        return res


#equal_lists
def equal_lists(ls1,ls2):
    are_eq=False
    if len(ls1)==len(ls2):
        for i in range(len(ls1)):
            if ls1[i]==ls2[i]:
                are_eq=True
            else:
                return False
        return are_eq
    else:
        return False
    
#count_item
def count_item(n,items):
    count=0
    for i in range(len(items)):
        if n==items[i]:
            count+=1
        else:
            pass
    return count

#take
def take(n,items):
    res=[]
    for i in range(0,min(n,len(items))):
        res+=[items[i]]
    return res

#drop
def drop(n,items):
    res=items
    for i in range(n):
        res.pop(0)
    return res


#reverse
def reverse(items):
    res=[]
    for i in items:
        res=[i]+res
    return res


def main():
    if __name__=='__main__':
        main()






