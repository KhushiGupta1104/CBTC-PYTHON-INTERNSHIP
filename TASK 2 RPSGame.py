print("\n_________________________ROCK PAPER SCISSOR GAME_________________________\n")

#Import Random Module 
import random

# Player Score
PScore = 0
# Computer Score
CScore = 0
#rounds
round=1

# A Tuple of options to be selected by Player and Computer
options = ("rock", "paper", "scissors")

# Function for Player's Choice
def get_player_choice():
    player = None
    while player not in options:
        player = input("Enter a choice (Rock, Paper, Scissors): ").lower()
        if player not in options:
            print("Invalid choice. Please try again.")
    print(f"Player: {player}")
    return player

# GAME ROUNDS
while round<=5:
    print(f"Round {round}")
    player = get_player_choice()
    computer = random.choice(options)
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a TIE in this round!\n")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("\nYou WIN this round!\n")
        PScore += 1
    else:
        print("\nYou LOSE this round!\n")
        CScore += 1
    round+=1

#COUNTING SCORES
print("Your Total Score:", PScore)
print("Computer Total Score:", CScore, "\n")

if PScore > CScore:
    print("Congratulations!! You are the WINNER.\n")
elif PScore < CScore:
    print("Sorry!! You have LOST.\n")
else:
    print("It is a TIE.\n")

print("Thanks for Playing!")

print("\n_______________________________GAME ENDED_________________________________\n")