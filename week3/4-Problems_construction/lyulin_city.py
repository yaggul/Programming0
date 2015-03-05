n=int(input("Моля въведете броя на блоковете: "))
m=0
blocks=[]
while m<n:
	blocks+=[int(input("Моля въведете височината на блоковете:"))]
	m+=1
#print(blocks)
highest=0
seen=[]
for i in blocks:
	if i>highest:
		seen+=[i]
		highest=i
print("Блоковете, които ще видите са с височина съответно {}".format(seen))
