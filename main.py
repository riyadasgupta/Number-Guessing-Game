import random

#Creating a function to generate a random number between 1 and 100
def generate_random_num():
    return random.randint(1, 100)

#Creating a function to get user's guess
def user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            else:
                return guess
        except ValueError:
            print("Please enter a valid integer.")

#Creating a function to check the guess and provide feedback
def check_guess(guess, secret_num):
    if guess < secret_num:
        return "Too low! Try again."
    elif guess > secret_num:
        return "Too high! Try again."
    else:
        return "Congratulations! You guessed the correct number!"

#Main play game function
def play_game():
    secret_num = generate_random_num()  # Generating secret number 
    guess_taken = 0                     # Counting how many guesses the player makes
    max_attempts = 10                   # Setting the limit for maximum attempts

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. You have 10 attempts to guess it!")

    while guess_taken < max_attempts:
        player_guess = user_guess()                     # Get player's guess
        guess_taken += 1
        
        result = check_guess(player_guess, secret_num)  # Checking the guess
        print(result)               
        
        if result.startswith("Congratulations"):
            print(f"You guessed the correct number in {guess_taken} attempts!")
            break
        
        #Notifying the player about remaining attempts
        remaining_attempts = max_attempts - guess_taken
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempt(s) left.")
        else:
            print(f"Sorry, you've used all {max_attempts} attempts! The correct number was {secret_num}.")
            break

# Calling the main play game function to start the game
play_game()
