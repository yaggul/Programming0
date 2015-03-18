#change_at
def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result

#change_at v2
def change_at2(index,ch,string):
    return string[0:index]+ch+string[index]


#reverse
def reverse(string):
    if string='':
        return ''
    else:
        res=''
        for i in string:
            res=i+res
    return res

#join
def join(delimiter,items):
    res=''
    for i in items:
        res+=str(i)
        res+=str(delimiter)
    return res[0:len(res)-1]

#startswith
def startswith(search,string):
    if string[0:len(search)]==search:
        return True
    else:
        return False

#endswith
def endswith(search,string):
    if string[len(string)-len(search):]==search:
        return True
    else:
        return False
    
#endswith v2
def endswith2(search,string):
    return startswith(reverse(search),reverse(string))

#trim
def trim(string):
    if string[0]==' ' and string[-1]==' ':
        return string[1:lent(string)-1]
    elif string[0]==' ':
        return string[1:]
    elif string[-1]==' ':
        return string[0:len(string)-1]
    else:
        return string
    
