n=int(input("Please insert a number: "))
m=1
collector=1
while m<n+1:
    collector*=m
    m+=1
print(collector)