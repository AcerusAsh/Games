import random
print("You and your opponent will have 100 health each")
print("You can either choose to strike or block")
print("Striking will do random damage ranging between 5 and 20")
print("Blocking will halve the oncoming damage from the opponent")
print("Goal is to take out the opponent")
input("Press any key to start\n")
while True:
    y = 100
    o = 100
    print("Your health: "+str(y))
    print("Opponent's health: "+str(o))
    while True:
        m = input("Enter S to strike or B to block\n")
        m=m.upper()
        b1 = 0
        b2 = 0
        if m == "S":
            yd = int(random.choice([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
        elif m == "B":
            yd = 0
            b1 = 1
        else:
            print("Invalid input\n")
            continue
        oc = int(random.choice([1,2]))
        if oc == 1:
            od = int(random.choice([5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
        else:
            od = 0
            b2 = 2
        if b1 == 1:
            y = y - (od/2)
        else:
            y = y - od
        if b2 == 2:
            o = o - (yd/2)
        else:
            o = o - yd
        print("Your health: "+str(y))
        print("Opponent's health: "+str(o))
        if y<=0 and o<=0:
            print("DRAW\n")
            break
        elif y<=0 and o>0:
            print("YOU LOSE !!!\n")
            break
        elif o<=0 and y>0:
            print("YOU WIN !!!\n")
            break
    rep = input("Would you like to play again? Enter yes to continue playing, enter anything else to stop\n")
    rep = rep.lower()
    if rep == "yes":
        continue
    else:
        print("Thanks for playing!!!")
        break






        


