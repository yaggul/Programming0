word=str(input("Please insert a word to search: "))
n=int(input("Please enter the number of words to search in: "))
count=1
words=[]
founder=0
while count<=n:
	wordsEL=input("Please enter a word: ")
	words=words+[wordsEL]
	count+=1
for i in words:
	if i==word:
		founder+=1
print("{} if found {} times.".format(word,founder))