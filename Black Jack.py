import random
print("Rules of the game\nYou and the dealer will be given a number\nYou can choose to hit or stand\nIf you hit, a that number will be increased by a random value between 2 and 13.\n")
print("If you choose to stand, your number won't change and the dealer's turn will begin\nThe goal is to have a number as close as possible to 21, but not greater than 21")
input("Press any key to play\n")
while True:
      y = int(random.choice([4,5,6,7,8,9,10.11,12,13,14,15,16,17,18,19,20,21]))
      print("Your number: "+str(y))
      d = int(random.choice([4,5,6,7,8,9,10.11,12,13,14,15,16,17,18,19,20,21]))
      print("Dealer's number: "+str(d))
      ys = 0
      ds = 0
      while True:
            if y == 21 and d == 21:
                   print("BOTH YOU AND DEALER GOT BLACKJACKS! IT'S A DRAW!!!")
                   break
            elif y!=21 and d == 21:
                   print("DEALER GOT A BLACKJACK! YOU LOST!!!")
                   break
            elif y==21 and d!=21:
                   print("YOU GOT A BLACKJACK! YOU WON!!!")
                   break
            if ys==0:
                  c = input("Enter H to hit or S to stand\n")
                  c=c.upper()
                  if c=="H":
                        print("YOU CHOSE TO HIT\n")
                        y = y + int(random.choice([2,3,4,5,6,7,8,9,10.11]))
                        print("Your number: "+str(y))
                        if y>21:
                              print("You LOSE")
                              break
                  elif c=="S":
                              print("YOU CHOSE TO STAND\n")
                              ys = 1         
                  else:
                              print("Invalid Input\n")
                              continue
            if ds==0:                     
                  dc = int(random.choice([1,2]))
                  if d>16:
                        dc = int(random.choice([1,2,3,4]))
                  if dc==1:
                        print("DEALER CHOSE TO HIT\n")
                        d = d + int(random.choice([2,3,4,5,6,7,8,9,10.11]))
                        print("Dealer's number: "+str(d)+"\n")
                        if d>21:                              
                              print("Dealer loses, you win")
                              break
                  else:
                        print("DEALER CHOSE TO STAND\n")
                        ds = 1
            if ys==0 or ds==0:
                  continue
            elif ys==1 and ds==1:
                  p = 21 - y
                  q = 21 - d
                  if p<q:
                        print("YOU WON!!!")
                        break
                  elif p>q:
                        print("DEALER WON!!!")
                        break
                  else:
                        print("Draw")
                        break
      pg = input("Enter yes if you want to play again, enter anything else if you don't\n")
      pg = pg.lower()
      if pg =="yes":
            continue
      else:
            print("Thanks for playing")
            break
