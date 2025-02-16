import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("Im thinking of a number between 1 and 50.")
    print("Try to guess it in as few attempts as possible.\n")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid number.")
            
# Start the game
guess_the_number()