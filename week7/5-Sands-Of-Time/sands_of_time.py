n=0
while n%2==0:
    n=int(input("Please insert an odd number: "))
ast='*'*n
mid=''
res=''
fill='.'
while len(ast)>0:
    mid=ast
    if len(ast)==n:
        res+=mid
        res+='\n'
    else:
        while len(mid)<n:
            mid=fill+mid
            mid=mid+fill
        res+=mid
        res+='\n'
    if len(ast)==1:
        break
    else:
        ast=ast[1:len(ast)-1]    
while len(ast)<=n:
    if len(ast)==n:
        break
    else:
        ast='*'+ast
        ast=ast+'*'
        mid=ast
        while len(mid)<n:
            mid=fill+mid
            mid=mid+fill
        res+=mid
        res+='\n'
print(res)
