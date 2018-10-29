# import the random package so that we can generate random numbers

from random import randint

player_lives = 3
computer_lives = 3

# choices is an array => a container that can hold multiple items

# arrays are 0-based -> the first item is 0, the second is 1, etc
print("Welcome to Rock, Paper, Scissors!")

choices = ["Rock", "Paper", "Scissors"]

player = False


# make the computer choose a weapon from the choices array at random

computer = choices[randint(0, 2)]


# print the choice to the terminal window

print("Computer chooses: ", computer, "\n")


while player is False:
    # set player to True
    print("Players Lives:", player_lives, "/3")
    print("Computer Lives:", computer_lives, "/3")
    print("Choose your weapon!")
    player = input("Rock, Paper, or Scissors?\n")
    print(player, "\n")

    if player == computer:
        print("Tie!\n")
    elif player == "Rock":
        if computer == "Paper":
            player_lives -= 1
            print("You lose!", computer, "covers", player, "\n")
        else:
            computer_lives -= 1
            print("You win!", player, "smashes", computer, "\n")
    elif player == "Paper":
        if computer == "Scissors":
            player_lives -= 1
            print("You lose!", computer, "cut", player, "\n")
        else:
            computer_lives -= 1
            print("You win!", player, "covers", computer, "\n")
    elif player == "Scissors":
        if computer == "Rock":
            player_lives -= 1
            print("You lose!", computer, "smashes", player, "\n")
        else:
            computer_lives -= 1
            print("You win!", player, "cut", computer, "\n")
    elif player == "quit":
        exit()
    
    else:

        print("Check your spelling... That's not a valid choice")

    if player_lives is 0:
        print("You are out of lives. Would you like to play again?")
        choice = input("Y / N")
        print(choice)

        if (choice is "Y") or (choice is "y"):
            player_lives = 3
            computer_lives = 3
            player = False
            computer = choices[randint(0, 2)]

        elif (choice is "N") or (choice is "n"):
            print("Thanks for playing!")
            exit()
    elif computer_lives is 0:
        print("Congratulations, you win! Would you like to play again?")
        choice = input("Y / N")

        if (choice is "Y") or (choice is "y"):
            player_lives = 3
            computer_lives = 3
            player = False
            computer = choices[randint(0, 2)]

        elif (choice is "N") or (choice is "n"):
            print("Thanks for playing!")
            exit()
    else:
        player = False
        computer = choices[randint(0, 2)]
