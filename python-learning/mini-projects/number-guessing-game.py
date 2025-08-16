import random

print("Welcome to the Number Guessing Game - By Steven")

while True:
    print("I'm thinking of a number from 1 and 100")

    secret_number = random.randint(1,100)
    attempts = 0

    while True:
        guess= input("Take a guess: ")
        guess = int(guess)
        attempts += 1
    
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"congratulations! You guesst it in {attempts} tries!")
        break
    
    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! Goodbye!")
        break