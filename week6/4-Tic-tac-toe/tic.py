board=[["X","O","#"],["X","X","X"],["#","#","#"]]


def board_to_string(board):
    count=0
    result1=''
    for i in board:
        count=0
        for j in i:
            if count in range(0,2):
                result1+='|'
                result1+=' '
                result1+=str(j)
                result1+=' '
            elif count==2:
                result1+='|'
                result1+=' '
                result1+=str(j)
                result1+=' '
                result1+='|'
                result1+='\n'            
            count+=1
    return(result1)


def main():
    if __name__=='__main__':
        main()
