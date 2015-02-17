import random
print("Welcome to Dice Game")
print()
N=int(input("Enter dice side: "))
p1name=str(input("Enter Player 1 name: "))
p2name=str(input("Enter Player 2 name: "))
p1roll=random.randint(1,N)
print(p1name+" rolls {}".format(p1roll))
p2roll=random.randint(1,N)
print(p2name+" rolls {}".format(p2roll))
print()
if p1roll>p2roll:
    print(p1name+" wins!")
elif p1roll<p2roll:
    print(p2name+" wins!")
else:
    print(p1name+" and "+p2name+" are even!")