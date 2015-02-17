N=int(input("Enter a number: "))
turn=1
collector=0
while turn<N+1:
    collector+=turn
    turn+=1
print(collector)