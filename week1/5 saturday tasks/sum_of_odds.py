N=int(input("\nPlease insert a number: "))
num=1
collector=0
while num<=N:
    if num%2==1:
        collector+=num
    num+=1
print(collector)