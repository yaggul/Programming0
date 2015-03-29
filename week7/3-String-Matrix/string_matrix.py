def string_matrix(matrix_width,strings):
    res=''
    for i in strings:
        start=0
        while start<=matrix_width:
            #start+=1
            while start<min(len(i),matrix_width):                                    
                for j in i:
                    if start<(min(len(i),matrix_width)):
                        res+='|'
                        res+=' '
                        res+=str(j)
                        res+=' '
                        start+=1
            if start<matrix_width:
                res+='|'
                res+=' '
                res+='X'
                res+=' '
                #start+=1
            elif start==matrix_width:
                res+='|'
                res+='\n'
            start+=1            
    print(res)
                
