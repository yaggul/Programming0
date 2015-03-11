def calculate_coins(sum):
	calc={100:0,50:0,20:0,10:0,5:0,2:0,1:0}
	cal=[100,50,20,10,5,2,1]
	index=0
	sum=int(sum*100)
	#print(sum)
	while sum>0:
		while sum-cal[index]>=0:
			calc[cal[index]]+=1
			sum=sum-cal[index]
		index+=1
		#print(calc)
	return calc


def main():
	if __name__=='__main__':
		main()
