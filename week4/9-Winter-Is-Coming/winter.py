def winter_is_coming(seasons):
    count=0
    start=0
    while start<len(seasons):
        if seasons[start]!='winter':
            count+=1
            start+=1            
        else:
            count=0
            start+=1
    if count>=5:
        return True
    else:
        return False
    
    
def main():
    if __name__=='__main__':
        main()
