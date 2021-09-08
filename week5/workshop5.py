import random

#==========================
#          Task 1
#==========================
def guess_random_number(tries, start, stop):
    num = random.randint(start, stop)
    while tries != 0:
        print("Number of tries left:", tries)
        while True:
            user_guess = input(f"Guess a number between {start} and {stop}: ")
            if user_guess.isdigit() and (start <= int(user_guess) <= stop):
                break
        user_guess = int(user_guess)
        if num == user_guess:
            print("You guessed the correct number!")
            return
        elif num > user_guess:
            print("Guess higher!")
        else: 
            print("Guess lower!")
        tries -= 1
    print(f"You have failed to guess the number: {num}")

guess_random_number(5, 0, 10)

#==========================
#          Task 2
#==========================
def guess_random_num_linear(tries, start, stop):
    num = random.randint(start, stop)
    print("The number for the program to guess is", num)
    for i in range(tries):
        print("Number of tries left", tries)
        print("The program is guessing...", i)
        if i == num:
            print("The program has guessed the correct number!")
            return
        tries -= 1
    print("The program has failed to guess the correct number.")

# guess_random_num_linear(5, 0, 10)

#==========================
#          Task 3
#==========================
def guess_random_num_binary(tries, start, stop):
    num = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop

    print("Random number to find:", num)
    while lower_bound <= upper_bound and tries != 0:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == num:
            print("Found it!", pivot)
            return
        elif pivot > num:
            print("Guessing lower")
            upper_bound = pivot -1
        else: 
            print("Guessing higher")
            lower_bound = pivot + 1
        tries -= 1
    print("Your program failed to find the number.")

# guess_random_num_binary(5, 0, 100)
