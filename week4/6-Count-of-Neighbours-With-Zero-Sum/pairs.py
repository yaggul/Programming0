def count_zero_neighbours(numbers):
	cnum=0
	count=0
	num=[]
	index=1
	while count<len(numbers)-1:
		if numbers[index]+numbers[index-1]==0:
			cnum+=1
			num+=[numbers[index],numbers[index-1]]
		else:
			pass
		index+=1
		count+=1
	return cnum,num
		
		
def main():
	if __name__=='__main__':
		main()
