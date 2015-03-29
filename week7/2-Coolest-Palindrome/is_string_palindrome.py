def is_string_palindrome(string):
    strcheck='abcdefghijklmnopqrstuvwxyz'
    string=string.lower()
    letonly=''
    res=''
    for i in string:
        if i in strcheck:
            letonly+=i
            res=i+res
    return letonly==res


def main():
    if __name__=='__main__':
        main()
