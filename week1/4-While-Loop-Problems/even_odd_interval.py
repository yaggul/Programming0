n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
start=min(n1,n2)
end=max(n1,n2)
while start<end+1:
    if start%2==0:
        print('{} - even'.format(start))
    else:
        print('{} - odd'.format(start))
    start+=1