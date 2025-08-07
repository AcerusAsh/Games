import random
while True:
      print("Rules of the game\nYou and the dealer will be given a number\nYou can choose to hit or stand\nIf you hit, a that number will be increased by a random value between 2 and 13.\n")
      print("If you choose to stand, your number won't change and the dealer's turn will begin\nThe goal is to have a number as close as possible to 21, but not greater than 21")
      input("Press any key to play\n")
      y = int(random.choice([1,2,3,4,5,6,7,8,9,10.11,12,13,14,15,16,17,18,19,20,21]))
      print("Your number: "+str(y))
      i = 0
      if y == 21:
            print("BLACK JACK !!! LUCKY WIN !!!")
            i = 3
      while(i==0):
            c = input("Enter H to hit or S to stand\n")
            c=c.upper()
            if c=="H":
                  y = y + int(random.choice([2,3,4,5,6,7,8,9,10.11,12,13]))
                  print("Your number: "+str(y))
                  if y>21:
                        print("You LOSE")
                        i = 5
                        break
            elif c=="S":
                        break
            else:
                        print("Invalid Input")
                        i = 1
      if (i==0):
            d = int(random.choice([1,2,3,4,5,6,7,8,9,10.11,12,13,14,15,16,17,18,19,20,21]))
            if d == 21:
                  print("Dealer got BLACK JACK !!! YOU LOSE !!!")
                  i = 4
            while (i==0):
                  dc = int(random.choice([1,2]))
                  if dc==1:
                        d = d + int(random.choice([2,3,4,5,6,7,8,9,10.11,12,13]))
                        if d>21:
                              print("Dealer's number: "+str(d))
                              print("Dealer loses, you win")
                              i = 2
                              break
                  else:
                        break
      if(i==0):
            print("Dealer's number: "+str(d))
            p = 21 - y
            q = 21 - d
            if p<q:
                  print("You win")
            elif p>q:
                  print("Dealer wins")
            else:
                  print("Draw")
      pg = input("Enter yes if you want to play again, enter anything else if you don't\n")
      pg = pg.lower()
      if pg =="yes":
            continue
      else:
            print("Thanks for playing")
            break
