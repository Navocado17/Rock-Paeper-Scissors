from kivy.app import App
import random

movelist = ["Rock", "Paper", "Scissors"]
playerSelectedMove = ""

class RockPaperScissors(App):
    pass

RockPaperScissors().run()


#Makes Random AI move and calcualtes the winner
def calculateWinner():
    selectedMove = movelist[random.randint(0,2)]
    print("Opponent chooses", selectedMove)
    selectedMove = selectedMove.lower()
    if playerSelectedMove == selectedMove:
        print(f"Both players selected {playerSelectedMove}. It's a tie!")
    elif playerSelectedMove == "rock":
        if selectedMove == "scissors":
           print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif playerSelectedMove == "paper":
        if selectedMove == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif playerSelectedMove == "scissors":
        if selectedMove == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

        
print("Welcome to rock paeper scissors game maen")
while True:    
    playerSelectedMove = input("Choose a Move: Rock, Paeper, Scissors: ")
    playerSelectedMove = playerSelectedMove.lower()
    calculateWinner()
