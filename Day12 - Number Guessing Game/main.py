import random
rand_number = random.randint(1,100)

def guess_check(guess):
    """
    This function checks how the guess close to the number computer is thinking of,
    or if the number and the guess is same or not.
    """
    global rand_number
    if guess == rand_number:
        print("You found the number! Congrats.")
        exit()

    if guess < rand_number - 10:
        print("Too low\nGuess again.")
    elif guess > rand_number + 10:
        print("Too high\nGuess again.")

def game(level):
    """
    level parameter is giving to this function from main function. 
    it defines the difficulty of this game. up to the level difficulty, attempt number is changed.
    """
    if level == "easy": 
        lives = 10
    elif level == "hard":
        lives = 5

    print(f"You have {lives} attempts remaining to guess number.")
    for count in range(lives):
        guess = int(input("Make a guess: "))
        guess_check(guess)
        print(f"You have {lives-1 - count} attempts remaining to guess number.")

def main():
    global rand_number
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. {rand_number}")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level != "hard" and level != "easy":
        print("undefined option.")
        exit()
    game(level)

main()
