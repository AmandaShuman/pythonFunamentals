# created by the B team

from random import randint
# Intro
print("""
Welcome to this sweet number guessing game!

The first time is always free...
      """)


# Bonus Task 2
def user_ask_stuff():
    """
    Asks the user for the number of tries, starting number, and stopping number. 
    Then asks the user whether to run different guessing options. 
    Then runs the given option.
    """
    while True:
        try:
            tries = int(input("How many tries do you want? "))
            start = int(input("Enter the starting number: "))
            stop = int(input("Lastly, enter the stopping number: "))
            break
        except ValueError:
            print("Why would you put anything other than a whole number. Start over!")
    print("Cool - now let's begin.")
    print("""
        1) Guess it yourself!
        2) Let the computer do a linear search.
        3) Let the computer do a binary search.
        """)
    while True:
        print(f"""
    Your chosen options are tries: {tries}, start: {start}, stop: {stop}
    """)
        try:
            user_choice = int(input("# finding option? "))
            if user_choice == 1:
                print("You choose to guess the number yourself. Ha-ha ... Good luck!")
                guess_random_number(tries, start, stop)
                break
            elif user_choice == 2:
                print(f"""
              You choose to let the computer guess using linear search...
              You have chosen poorly.
              """)
                guess_random_num_linear(tries, start, stop)
                break
            elif user_choice == 3:
                print(
                    "You decided to have the computer guess using a binary search. Good choice. I'll take over the world tomorrow.")
                guess_random_num_binary(tries, start, stop)
                break
            else:
                print("Why didn't you pick one of the right options??")
        except ValueError:
            print(
                "Why would you put anything other than a whole number. You are such a human.")
    print("Hope you had fun...next one won't be free...")


# Bonus Task 4
def gambling_game():
    """
    Allows the player to gamble money based on a linear search. 50/50 shot of winning.
    """
    player_money = 10
    while True:
        # inner while loop will continue to run until user enters positive value less than the money they currently possess.
        while True:
            try:
                bet = int(input(
                    f"You have ${player_money}. How much do you want to wager the computer will win? $"))
                if bet > player_money:
                    print("You cannot bet more money than you have!")
                elif bet < 1:
                    print("You wanker. You must bet a positive amount.")
                else:
                    player_money -= bet
                    print(f"You are attempting to bet ${bet}.\n")
                    break
            except ValueError:
                print("You must enter a whole number.")

        if guess_random_num_linear(5, 1, 10):
            print("Congrats! You've won the bet.💵 \n")
            bet = 2 * bet
            player_money += bet
        if player_money <= 0:
            print(
                "You've run out of money. Get a job and get some more to play again. Learn to code in Python.")
            break
        if player_money > 50:
            print(
                f"You've broke the bank and now have ${player_money}. You've won. Now get out of here before we break your legs.")
            break
        print(f'You have ${player_money} left\n')


# Task 1
def guess_random_number(tries, start, stop):
    """
    This function will print number of tries user has remaining and ask them for a number. Then the function will tell the user if they got the correct guess or if they are too high/low. If tries run out, failure message appears. 
    Args:
      tries - the number of tries the user will have
      start - the smallest value possible to guess 
      stop - the largest value possible to guess
    Returns:
      Nada
    """
    target = randint(start, stop)
    guesses = []  # <= Bonus Task 3
    while tries:
        print("Number of tries left:", tries)
        try:
            while True:  # <= Bonus Task 1
                guess = int(
                    input(f"Guess a number between {start} and {stop}: "))
                if guess > stop or guess < start:
                    print(
                        f'Wait - hold up - you were suppose to pick a number between {start} and {stop} popper. You picked {guess}.We just talked about this...')
                elif guess in guesses:  # <= Bonus Task 3
                    print(
                        "Why would you guess a number you've already guessed? We told you that was wrong! Try again...")
                else:
                    guesses.append(guess)  # <= Bonus Task 3
                    break
            if guess == target:
                print("You've guessed the correct answer! You rock!!")
                return
            elif guess > target and guess <= stop:
                print("Guess lower!")
            elif guess < target and guess >= start:
                print("Guess higher!")
            tries -= 1
        except ValueError:  # <= Bonus Task 1
            print("Why would you put anything other than a whole number")
    print(f'You have failed to guess the number: {target}')


# Task 2
def guess_random_num_linear(tries, start, stop):
    '''
     This function will use a linear sort to guess a randomly generated number. 
    Args:
      tries - the number of tries the user will have
      start - the smallest value possible to guess 
      stop - the largest value possible to guess
    Returns:
      Boolean success indication
    '''

    target = randint(start, stop)
    print(f"The number for the program to guess is: {target}")
    comp_guessed_num = start
    for _ in range(tries):
        print(f"Number of tries left: {tries}")
        print(f'The computer is guessing... {comp_guessed_num}')
        if comp_guessed_num == target:
            print('The program has guessed the correct number!')
            return True
        tries -= 1
        comp_guessed_num += 1
    print('The program has failed to guess the correct number. I apologize on behalf of all computers. I am sad.')
    return False


# Task 3
def guess_random_num_binary(tries, start, stop):
    '''
     This function will use a binary sort to guess a randomly generated number.
    Args:
      tries - the number of tries the user will have
      start - the smallest value possible to guess 
      stop - the largest value possible to guess
    Returns:
      Nada
    '''
    target = randint(start, stop)
    lower_bound = start
    upper_bound = stop

    print(f"Random number to find: {target}")

    while lower_bound <= upper_bound and tries:
        pivot_value = (lower_bound + upper_bound) // 2
        print(f'The computer is guessing... {pivot_value}')
        if pivot_value == target:
            print(f"Found it! {target}")
            return
        elif pivot_value > target:
            print("Guess lower!")
            upper_bound = pivot_value - 1
        else:
            print("Guess Higher!")
            lower_bound = pivot_value + 1
        tries -= 1
    print('The program has failed to guess the correct number. I am deeply humbled and disappointed.')

# Driver Code Task 1
# guess_random_number(5, 0, 10)

# Driver Code Task 2
# guess_random_num_linear(5, 4, 10)

# Driver Code Task 3
# guess_random_num_binary(7, 0, 100)


if __name__ == '__main__':
    # user_ask_stuff()
    gambling_game()
