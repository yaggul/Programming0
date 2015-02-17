import random
a=1
b=int(input("Enter sides: "))
def roll(a,b):
    rnd=1
    collector=0
    while rnd<4:
        print()
        input("Press ENTER to roll the dice...")
        print()
        turn=random.randint(a,b)
        if rnd==1:
            print("First roll: {}".format(turn))
            #print(turn)
            #rnd+=1
            #collector+=turn
        elif rnd==2:
            print("Second roll: {}".format(turn))
            #print(turn)
            #rnd+=1
            #collector+=turn
        elif rnd==3:
            print("Third roll: {}".format(turn))
            #print(turn)
        rnd+=1
        collector+=turn
    print("Sum is: {}".format(collector))
roll(a,b)