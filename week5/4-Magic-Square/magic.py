def magic_square(square):
    ''' 
        [23,28,21]
        [22,24,26]
        [27,20,25]'''
       
       
    row=0
    col=0
    collector=[]
    ssum=0
    while row<len(square):
        for i in square[row]:
            ssum+=i
        collector+=[ssum]
        ssum=0
        row+=1
    row=0
    col=0
    ssum=0
    
    while col<len(square):
        while row<len(square):
            ssum+=square[row][col]
            row+=1
        collector+=[ssum]
        ssum=0
        row=0
        col+=1
    row=0
    col=0
    ssum=0
    while row<len(square):
        ssum+=square[row][col]
        row+=1
        col+=1
    collector+=[ssum]
    row=-1
    col=-1
    ssum=0
    while row>-len(square)-1:
        ssum+=square[row][col]
        row-=1
        col-=1
    collector+=[ssum]
    if collector.count(collector[0])==8:
        return True,collector
    else:
        return False,collector
        
        
        
        
def main():
    if __name__=='__main__':
        main()
    
    
