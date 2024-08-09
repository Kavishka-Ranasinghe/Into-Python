from datetime import datetime
import random
import sys

def chance(name):
    print(str(name)+"'s Chance now")
    number = random.randint(1, 10)
    print(str(name) + " scored "+str(number)+" mark")
    return number
def game():
    tot01 = 0
    tot02 = 0

    for i in range(1, 6):

        print("Round: "+str(i))
        ans = input("Do you want to continue? ('y' yes 'n' no) : ")
        if ans == "y":
           tot01 = chance("player01") + tot01
           print("player 01's current score is "+str(tot01))
           print("")
           tot02 = chance("player02") + tot02
           print("player 02's current score is " + str(tot02))
           print("")
        elif ans == "n":
            print("Match is ended in round "+str(i))
            print("")
            print("let's decide the winner")
            dec(tot01, tot02)
            input("Press enter to exit")
            sys.exit()

        else:
            print("Invalid input , Game ended :(")
            input("Press enter to exit")
            sys.exit()

    print("Match is ended in 5 rounds.")
    print("let's decide the winner")
    dec(tot01, tot02)
    input("Press enter to exit")


def dec(tot01, tot02):

 if tot01 > tot02:
      print("player 01 is the winner with "+str(tot01)+" marks and player 02 loosed with having "+str(tot02)+" marks")
      
 elif tot01 & tot02 == 0:
     print("Both loosed by scoring " + str(tot01)+" marks")

 elif tot01 == tot02:
      print("match is a draw both scored same marks "+str(tot01))

 else:
      print("player 02 is the winner with "+str(tot02)+" marks and player 01 loosed with having "+str(tot01)+" marks")


now = datetime.now()
t = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", t)
print("Welcome to random number generator")
print("Game consist of 5 rounds, each time random number from 1-10 will be generated.")
print("Person with highest score wins !!!")
decision = str(input("please enter letter 'p' to continue and press 'e' to exit."))
print("")

if decision == "p":
    game()


elif decision == "e":
    print("Game ended")
    input("Press enter to exit")

else:
    print("Invalid input")
    input("Press enter to exit")
