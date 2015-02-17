print()
N=int(input("Please insert a number: "))
num=1
collector=0
while num<=N:
    if num%2==0:
        collector+=num
    num+=1
print(collector)