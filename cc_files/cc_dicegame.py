import random
import sys

high_score = 0

def dice_roll_2x():
    global high_score
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    print("\n You roll a...", roll1)
    print("You roll a...", roll2, "\n")
    print(f"You have rolled a total of {roll1 + roll2} \n")
    if roll1 + roll2 > high_score:
        print("New high Score! \n")
        high_score = roll1 + roll2

def exit_game():
    print("Goodbye!")
    sys.exit()

def reset_game():
    global high_score
    new_game = input("You have maxed out the high score! Want to play again? Yes/No?    ")
    if new_game.lower().strip() == "yes":
        print("\n\nNew game!")
        high_score = 0
    else:
        sys.exit()

def dice_game(): 
    while True:
        global high_score
        print("Current High Score:", high_score)
        print("1) Roll Dice \n2) Leave Game")
        choice = input("Enter your choice: ")
        if choice == "1":
            dice_roll_2x()
            if high_score == 12:
                reset_game()           
        elif choice == "2":
            exit_game()
        else:
            print("You have entered an invalid choice. Try again.")

dice_game()
