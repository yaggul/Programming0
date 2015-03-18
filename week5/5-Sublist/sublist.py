def sublist(list1,list2):
	'''[1,2,3]
	[0,0,1,2,3,4,5,6]'''
	l1=''
	l2=''
	for i in list1:
		l1+=str(i)
	for j in list2:
		l2+=str(j)
	if l1 in l2:
		return True
	else:
		return False


def sublist2(list1,list2):
    start=0
    res=[]
    collector=[]
    while start<len(list2)-len(list1)+1:
        print(start)
        for i in range(start,start+len(list1)):
            collector+=[list2[i]]
        print(collector)
        if collector==list1:
            return True
        else:
            collector=[]
        start+=1
    return False






def main():
	if __name__=='__main__':
		main()
