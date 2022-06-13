#Rock, Paper, and Scissors Game
#Import random
import random

while True:
    choices = ["r","p","s"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors\n").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "r":
        if computer == "p":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "s":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
    elif player == "s":
        if computer == "r":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "p":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
    elif player == "p":
        if computer == "s":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose!")
        if computer == "r":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win!")
    play_again = input("Play again? (yes/no) : ").lower()

    if play_again != "yes":
         break

print("Bye!")