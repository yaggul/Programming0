word=input("Please insert  a string: ")
vowels=['a','e','i','o','u','y','A','E','I','O','U','Y']
collector=[]
for i in word:
	if i in vowels:
		collector+=[i]
print("The count of vowels in \"{}\" is {}.".format(word,len(collector)))
print("The vowels are {}.".format(collector))