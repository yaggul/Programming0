def inner_trim(string):
    "  lalalalal   lalalala   lalalala  "
    count=0
    res=''
    for i in string:
        if i==' ' and count==0:
            res+=' '
            count=1
        elif i!=' ':
            res+=i
            count=0
        else:
            pass
    if res[0]==' ' and res[-1]==' ':
        res=res[1:len(res)-1]
    elif res[0]==' ':
        res=res[1:]
    elif res[-1]==' ':
        res=res[:len(res)-1]
    else:
        pass
    return res


def main():
    if __name__=='__main__':
        main()
