import random
from itertools import combinations
input("Welcome to poker 5 Card draw! Press any key to start\n")
def play():
    yh = []
    oh = []
    allc = (['2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS','AS','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD','AD','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH','AH','2C','3C','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC','AC'])
    yh = random.sample(allc,5)
    for a in range(0,5):
        allc.remove(yh[a])
    oh = random.sample(allc,5)
    for a in range(0,5):
        allc.remove(oh[a])
    print("Your Hand: ")
    print(yh)
    while True:
        choice = input("Enter K to keep your hand or S to swap cards?\n")
        choice = choice.upper()
        if choice == 'K':
            print("You decided to keep your hand\n")
            break
        elif choice == 'S':
            while True:
                cards = input("Which cards would you like to swap? You can swap upto three. Enter in this format: card1,card2, etc.\n")
                swapc = []
                if len(cards)>3:
                    swapc = cards.split(",")
                else:
                    swapc.append(cards)
                if len(swapc)>3:
                    print("Invalid input, try again")
                    continue
                else:
                    if all(t in yh for t in swapc):
                        for a in range(0,len(swapc)):
                            yh.remove(swapc[a])
                        newc = random.sample(allc,len(swapc))
                        for a in range(0,len(newc)):
                            yh.append(newc[a])
                        for a in range(0,len(newc)):
                            allc.remove(newc[a])
                        break
                    else:
                        print("Cards not found, try again\n")
                        continue
            break
        else:
            print("Invalid input, try again\n")
            continue
    ochoice = random.choice([1,2])
    if ochoice == 1:
        oco = int(random.choice([1,2,3]))
        orc = random.sample(oh,oco)
        for a in range(0,oco):
            oh.remove(orc[a])
        noc = random.sample(allc,oco)
        for a in range(0,oco):
            oh.append(noc[a])
        for a in range(0,oco):
            allc.remove(noc[a])
    order = ["AS","AD","AH","AC","KS","KD","KH","KC","QS","QD","QH","QC","JS","JD","JH","JC","10S","10D","10H","10C","9S","9D","9H","9C","8S","8D","8H","8C","7S","7D","7H","7C","6S","6D","6H","6C","5S","5D","5H","5C","4S","4D","4H","4C","3S","3D","3H","3C","2S","2D","2H","2C",]
    cmap1 = {item: i for i, item in enumerate(order)}
    yh.sort(key = lambda x: cmap1[x])
    print("Your final hand: ")
    print(yh,"\n")
    cmap2 = {item: i for i, item in enumerate(order)}
    oh.sort(key = lambda x: cmap2[x])
    yl = 0
    ol = 0
    seq = "AKQJ1098765432"
    yseq = yh[0][0] + yh[1][0] + yh[2][0] + yh[3][0] + yh[4][0]
    oseq = oh[0][0] + oh[1][0] + oh[2][0] + oh[3][0] + oh[4][0]
    def isstraight(aseq):
        return aseq in seq
    def isflush(hand):
        if all('S' in s for s in hand) or all('D' in s for s in hand) or all('H' in s for s in hand) or all('C' in s for s in hand):
            return True
        else:
            return False
    def isofkind(hand):
        if all('2' in s for s in hand) or all('3' in s for s in hand) or all('4' in s for s in hand) or all('5' in s for s in hand) or all('6' in s for s in hand) or all('7' in s for s in hand) or all('8' in s for s in hand) or all('9' in s for s in hand) or all('10' in s for s in hand) or all('J' in s for s in hand) or all('Q' in s for s in hand) or all('K' in s for s in hand) or all('A' in s for s in hand):
            return True
        else:
            return False
    def isfullhouse(hand):
        count = 0
        for combo in combinations(hand,3):
            if isofkind(combo):
                temp = hand[:]
                temp.remove(combo[0])
                temp.remove(combo[1])
                temp.remove(combo[2])
                for combo1 in combinations(temp,2):
                    if isofkind(combo1):
                        return True
                    else:
                        count = count + 1
                    if isofkind(combo1) == False and count == 2:
                        return False
        else:
            return False
    def istwopair(hand):
        count = 0
        for combo in combinations(hand,2):
            if isofkind(combo):
                temp1 = hand[:]
                temp1.remove(combo[0])
                temp1.remove(combo[1])
                for combo1 in combinations(temp1,2):
                    if isofkind(combo1):
                        return True
                    else:
                        count= count + 1
                    if isofkind(combo1)==False and count==2:
                        return False
            else:
                return False
    def isfourofkind(hand):
        count = 0
        for combo in combinations(hand,4): 
            if isofkind(combo):
                return True
            else:
                count = count + 1
            if isofkind(combo)==False and count==5:
                return False
    def isthreeofkind(hand):
        count = 0
        for combo in combinations(hand,3): 
            if isofkind(combo):
                return True
            else:
                count = count + 1
            if isofkind(combo)==False and count==10:
                return False
    def ispair(hand):
        count = 0
        for combo in combinations(hand,2): 
            if isofkind(combo):
                return True
            else:
                count = count + 1
            if isofkind(combo)==False and count==10:
                return False
    if ("A" in yh[0]) and ("K" in yh[1]) and ("Q" in yh[2]) and ("J" in yh[3]) and ("10" in yh[4]) and isflush(yh):
        yl = 10
        print("You got a ROYAL FLUSH!!!\n")
    elif isstraight(yseq) and isflush(yh):
        yl = 9
        print("You got a straight flush!\n")
    elif isfourofkind(yh):
        yl = 8
        print("You got four of a kind!\n")
    elif isfullhouse(yh):
        yl = 7
        print("You got full house!\n")
    elif isflush(yh):
        yl = 6
        print("You got a flush!\n")
    elif isstraight(yseq):
        yl = 5
        print("You got a straight!\n")
    elif isthreeofkind(yh):
        yl = 4
        print("You got three of a kind!\n")
    elif istwopair(yh):
        yl = 3
        print("You got two pairs!\n")
    elif ispair(yh):
        yl = 2
        print("You got a pair!\n")
    else:
        yl = 1
        print("You got High card!\n")
    if ("A" in oh[0]) and ("K" in oh[1]) and ("Q" in oh[2]) and ("J" in oh[3]) and ("10" in oh[4]) and isflush(oh):
        ol = 10
        print("Opponent got a ROYAL FLUSH!!!\n")
    elif isstraight(oseq) and isflush(oh):
        ol = 9
        print("Opponent got a straight flush!\n")
    elif isfourofkind(oh):
        ol = 8
        print("Opponent got four of a kind!\n")
    elif isfullhouse(oh):
        ol = 7
        print("Opponent got full house!\n")
    elif isflush(oh):
        ol = 6
        print("Opponent got a flush!\n")
    elif isstraight(oseq):
        ol = 5
        print("Opponent got a straight!\n")
    elif isthreeofkind(oh):
        ol = 4
        print("Opponent got three of a kind!\n")
    elif istwopair(oh):
        ol = 3
        print("Opponent got two pairs!\n")
    elif ispair(oh):
        ol = 2
        print("Opponent got a pair!\n")
    else:
        ol = 1
        print("Opponent got High card!\n")
    print("Opponent's hand: \n")
    print(oh,"\n")
    if(yl>ol):
        print("YOU WON!!!\n")
    elif(ol>yl):
        print("YOU LOST!!!\n")
    elif(yl==1 and ol == 1):
        if(yh[0][0] > oh[0][0]):
            print("YOU WON!!!")
        elif(oh[0][0] > yh[0][0]):
            print("YOU LOST!!!\n")
        else:
            print("IT'S A TIE!!!\n")
    else:
        print("IT'S A TIE!!!\n")
play()
while True:
    resp = input("Enter yes to play again or enter anything else to stop playing\n")
    resp = resp.lower()
    if resp == "yes":
        play()
    else:
        break
