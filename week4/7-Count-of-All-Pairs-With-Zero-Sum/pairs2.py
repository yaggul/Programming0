def count_zero_pairs(items):
    cnum=0
    nums=[]
    for i in range(0,len(items)):
        for j in range(i,len(items)):
            if items[i]+items[j]==0:
                if items[i] in nums or items[j] in nums:
                    pass
                else:
                    cnum+=1
                    nums+=[items[i]]+[items[j]]
                
    return cnum,nums


def main():
    if __name__=='__main__':
        main()
