def count_vowels_consonants(word):
	vowels='aeiouyAEIOUY'
	consonants='bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ'
	count={'vowels':0,'consonants':0}
	for i in word:
		if i in vowels:
			count['vowels']+=1
		else:
			count['consonants']+=1
	return count

def main():
	if __name__=='__main__':
		main()
