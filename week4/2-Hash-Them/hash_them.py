def hash_them(keys,values):
	hashtbl={}
	index=0
	while index<len(keys):
		while index<len(values):
			hashtbl[keys[index]]=values[index]
			index+=1
		hashtbl[keys[index]]=None
		index+=1
	return hashtbl

def main():
	if __name__=='__main__':
		main()
