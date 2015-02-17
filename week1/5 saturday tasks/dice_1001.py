from random import randint
p1Score=1001
p2Score=1001
p1Roll=0
p2Roll=0
p1Name=str(input("Player 1 enter your name: ")).capitalize()
p2Name=str(input("Player 2 enter your name: ")).capitalize()
dRound=1
while p1Score!=0 and p2Score!=0:
    print("\nRound No {}".format(dRound))
    input("\n{} press ENTER to roll the dices".format(p1Name))
    p1Roll=randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)
    print("{} rolls {}".format(p1Name,p1Roll))
    if p1Score>0:
        p1Score-=p1Roll
    else:
        p1Score+=p1Roll
    #if p1Score==0:
    #    break
    #else:
    #    pass
    print("{} temp score is {}.".format(p1Name,p1Score))
    input("\n{} press ENTER to roll the dices".format(p2Name))
    p2Roll=randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)+randint(1,6)
    print("{} rolls {}".format(p2Name,p2Roll))
    if p2Score>0:
        p2Score-=p2Roll
    else:
        p2Score+=p2Roll
    #if p2Score==0:
    #    break
    #else:
    #    pass
    print("{} temp score is {}.".format(p2Name,p2Score))
    dRound+=1
print("\nGame OVER\n")
if p1Score==0:
    print("{} score is {}".format(p1Name,p1Score))
    print("{} score is {}".format(p2Name,p2Score))
    print("{} is the winner".format(p1Name))
elif p2Score==0:
    print("{} score is {}".format(p1Name,p1Score))
    print("{} score is {}".format(p2Name,p2Score))
    print("{} is the winner".format(p2Name))
elif p1Score==0 and p2Score==0:
    print("{} and {} are even. Let's play again.".format(p1Name,p2Name))