import random

#Ska finnas globala variabler för vunna rundor och för matcher vunna för både datorn och spelaren
playerWins = 0
computerWins = 0

playerRoundWins = 0
computerRoundWins = 0

def informOfValueError():
    print("-"*20)
    print("Du måste välja ett nummer!")
    print("-"*20)

#resultOfDraw() skriver ut vad som händer vid oavgjort
def resultOfDraw():
    print("Det blev oavgjort!")

#resultOfPlayerWin() ändrar spelarens antal vinster och presenterar vinnare
def resultOfPlayerWin():
    global playerRoundWins
    playerRoundWins = playerRoundWins + 1
    print("Du vann denna runda!")

#resultOfComputerWin() ändrar datorns antal vinster och presenterar vinnare
def resultOfComputerWin():
    global computerRoundWins
    computerRoundWins = computerRoundWins + 1
    print("Datorn vann denna runda!")

#calculateWinner() genom if-satser kolla vem som vinner
def calculateWinner(playerChoice, computerChoice):
    #comparing the choices
    if(playerChoice==computerChoice):
        resultOfDraw()
    elif(playerChoice==1 and computerChoice==3) or (playerChoice==2 and computerChoice==1) or (playerChoice==3 and computerChoice==2):
        resultOfComputerWin()
    else:
        resultOfPlayerWin()

#function that handles if-statement to deliver the news of the computers choice
def choiceToString(num):
    if(num==1):
        return "sten"
    elif(num==2):
        return "sax"
    else:
        return "påse"

#oneRound() ska kontrollera en "sten sax påse" runda
def oneRound():
    try:
        playerChoiceNum = int(input("Gör ditt val genom att välja ett nummer:\n1. Sten\n2. Sax\n3. Påse\nEnter choice: "))
        if(playerChoiceNum in [1,2,3]):
            computerChoiceNum = random.randrange(1,4)
            print(f"Du valde: {choiceToString(playerChoiceNum)}\nDatorn valde{choiceToString(computerChoiceNum)}")
            calculateWinner(playerChoiceNum,computerChoiceNum)
            print("-"*20)
            print(f"\t     Ställning")
            print(f"\tDu\t\tDator")
            print(f"\t{playerRoundWins}\t\t  {computerRoundWins}")
            print("-"*20)
        else:
            print("-"*20)
            print("Du måste välja 1, 2 or 3")
            print("-"*20)
            oneRound()
    except ValueError:
        informOfValueError()
        oneRound()

#wantsToPlatAgain() checks and returns wether the player wants to play again
def wantsToPlayAgain():
    try:
        answer = int(input("Vill du spela igen?\n1.Ja\n2.Nej\nSkriv siffra som svar: "))
        if(answer==1):
            return True
        elif(answer==2):
            return False
        else:
            print("-"*20)
            print("Du måste välja 1 eller 2")
            print("-"*20)
            wantsToPlayAgain()
    except ValueError:
        informOfValueError()
        wantsToPlayAgain()


#main() ska introducera spelet och hålla en loop för flera rundor
def main():
    #Definierar globala variabler för main()
    global playerWins
    global computerWins
    global playerRoundWins
    global computerRoundWins

    #while-loop som körs tills spelaren inte längre vill spela
    wantsToPlay = True
    while(wantsToPlay):
        try:
            rounds = int(input("Hur många rundor \"bäst av\" vill du köra? Det måste vara ett UDDA nummer!\nSkriv antal rundor: "))
            if(rounds%2==1):
                neededRoundsToWin = int((rounds+1)/2)
                print("-"*20)
                print(f"Välkommen till sten, sax, påse! Du kommer spela {neededRoundsToWin} rundor.\nDu spelar mot datorn.")
                print("-"*20)
                #while-loop som körs tills någon vunnit "bäst av..."
                while(playerRoundWins!=neededRoundsToWin and computerRoundWins!=neededRoundsToWin):
                    #Anropar en runde per loop
                    oneRound()
                if(playerRoundWins>computerRoundWins):
                    playerWins = playerWins+1
                    print("Du vann! ^-^")
                else:
                    computerWins = computerWins+1
                    print("Datorn vann -_-'")
                playerRoundWins = 0
                computerRoundWins = 0
                wantsToPlay = wantsToPlayAgain()
                #Uppdatera statsen på matcher vunna
                print(f"Av alla era matcher är nu:\nDin poäng {playerWins}\nDatorns poäng {computerWins}")
            else:
                print("-"*20)
                print("Nummret måste vara udda!!!!")
                print("-"*20)
        except ValueError:
            informOfValueError()

main()